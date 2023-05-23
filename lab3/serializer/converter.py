import base64
import builtins
import inspect

from lab3.serializer.constants import PRIMITIVE_TYPES, BYTES_TYPE, TUPLE_TYPE, SET_TYPE, \
    FUNCTION_TYPE, CELL_TYPE, CODE_TYPE, UNSERIALIZABLE_CODE_TYPES, MODULE_TYPE, CLASS_TYPE, UNSERIALIZABLE_DUNDER, \
    UNSERIALIZABLE_TYPES, ITERATOR_TYPE, PROPERTY_TYPE
from types import FunctionType, MethodType, CellType, CodeType, ModuleType


class Converter:
    @classmethod
    def convert(cls, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj

        if isinstance(obj, list):
            return type(obj)(cls.convert(item) for item in obj)

        if isinstance(obj, dict):
            return {key: cls.convert(value) for key, value in obj.items()}

        if isinstance(obj, bytes):
            return cls._convert_bytes(obj)

        if isinstance(obj, (tuple, set)):
            return cls._convert_collections(obj)

        if isinstance(obj, (FunctionType, MethodType)):
            return cls._convert_function(obj)

        if isinstance(obj, CellType):
            return cls._convert_cell(obj)

        if isinstance(obj, CodeType):
            return cls._convert_code(obj)

        if isinstance(obj, ModuleType):
            return cls._convert_module(obj)

        if isinstance(obj, type):
            return cls._convert_class(obj)

        if cls._is_iterable(obj):
            return cls._convert_iterator(obj)

        if isinstance(obj, property):
            return cls._convert_property(obj)

        else:
            raise Exception(f"The {type(obj).__name__} type conversion is not implemented")

    @classmethod
    def convert_back(cls, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj

        if isinstance(obj, list):
            return type(obj)(cls.convert_back(item) for item in obj)

        if isinstance(obj, dict):
            decode_type = cls._get_type(obj)

            if decode_type is None:         # dictionary case
                return {key: cls.convert_back(value) for key, value in obj.items()}
            if decode_type == BYTES_TYPE:
                return cls._convert_back_bytes(obj)
            if decode_type in (TUPLE_TYPE, SET_TYPE):
                return cls._convert_back_collections(obj)
            if decode_type == FUNCTION_TYPE:
                return cls._convert_back_function(obj)
            if decode_type == CELL_TYPE:
                return cls._convert_back_cell(obj)
            if decode_type == CODE_TYPE:
                return cls._convert_back_code(obj)
            if decode_type == MODULE_TYPE:
                return cls._convert_back_module(obj)
            if decode_type == CLASS_TYPE:
                return cls._convert_back_class(obj)
            if decode_type == ITERATOR_TYPE:
                return cls._convert_back_iterator(obj)
            if decode_type == PROPERTY_TYPE:
                return cls._convert_back_property(obj)
        raise Exception(f'The {decode_type} type back conversion is not implemented')

    @classmethod
    def _convert_bytes(cls, obj: bytes):
        data = base64.b64encode(obj).decode('ascii')
        return cls._create_dict(data, BYTES_TYPE)

    @classmethod
    def _convert_back_bytes(cls, obj):
        return base64.b64decode(cls._get_data(obj).encode('ascii'))

    @classmethod
    def _convert_collections(cls, obj):
        data = [cls.convert(item) for item in obj]
        return cls._create_dict(data, type(obj).__name__.lower())

    @classmethod
    def _convert_back_collections(cls, obj):
        data = cls._get_data(obj)
        collection = getattr(builtins, cls._get_type(obj).lower())
        return collection(cls.convert_back(item) for item in data)

    @classmethod
    def _convert_function(cls, obj):
        func_code = obj.__code__
        func_name = obj.__name__
        func_defaults = obj.__defaults__
        func_dict = obj.__dict__
        func_class = cls._get_methods_father_class(obj)
        func_closure = (
            tuple(cell for cell in obj.__closure__ if cell.cell_contents is not func_class)
            if obj.__closure__ is not None
            else tuple()
        )
        func_globals = {
            key: cls.convert(value)
            for key, value in obj.__globals__.items()
            if key in obj.__code__.co_names
            and value is not func_class
            and key != obj.__code__.co_name
        }

        converted_func = cls.convert(
            dict(
                code=func_code,
                name=func_name,
                argdefs=func_defaults,
                closure=func_closure,
                func_dict=func_dict,
                globals=func_globals
            )
        )
        return cls._create_dict(converted_func, FUNCTION_TYPE, is_method=isinstance(obj, MethodType))

    @classmethod
    def _convert_back_function(cls, obj):
        converted_func = cls.convert_back(cls._get_data(obj))

        func_dict = converted_func.pop('func_dict')

        new_func = FunctionType(**converted_func)
        new_func.__dict__.update(func_dict)
        new_func.__globals__.update({new_func.__name__: new_func})
        return new_func

    @classmethod
    def _convert_cell(cls, obj):
        data = cls.convert(obj.cell_contents)
        return cls._create_dict(data, CELL_TYPE)

    @classmethod
    def _convert_back_cell(cls, obj):
        return cls._make_cell(cls.convert_back(cls._get_data(obj)))

    @classmethod
    def _convert_code(cls, obj):
        attrs = [attr for attr in dir(obj) if attr.startswith('co')]

        code_dict = {
            attr: cls.convert(getattr(obj, attr))
            for attr in attrs
            if attr not in UNSERIALIZABLE_CODE_TYPES
        }

        return cls._create_dict(code_dict, CODE_TYPE)

    @classmethod
    def _convert_back_code(cls, obj):
        data = cls._get_data(obj)

        def func():
            pass

        code_dict = cls.convert_back(data)
        return func.__code__.replace(**code_dict)

    @classmethod
    def _convert_module(cls, obj):
        return cls._create_dict(obj.__name__, MODULE_TYPE)

    @classmethod
    def _convert_back_module(cls, obj):
        return __import__(cls._get_data(obj))

    @classmethod
    def _convert_class(cls, obj):
        data = {
            attr: cls.convert(getattr(obj, attr))
            for attr, value in inspect.getmembers(obj)
            if attr not in UNSERIALIZABLE_DUNDER
            and type(value) not in UNSERIALIZABLE_TYPES
        }

        data['__bases__'] = [
            cls.convert(base) for base in obj.__bases__ if base != object
        ]

        data['__name__'] = obj.__name__

        return cls._create_dict(data, CLASS_TYPE)

    @classmethod
    def _convert_back_class(cls, obj):
        data = cls._get_data(obj)

        class_bases = tuple(cls.convert_back(base) for base in data.pop('__bases__'))

        class_dict = {
            attr: cls.convert_back(value)
            for attr, value in data.items()
            if not (isinstance(value, dict) and cls._get_type(value) == FUNCTION_TYPE)
        }

        decoded_class = type(data['__name__'], class_bases, class_dict)

        for key, value in data.items():
            if isinstance(value, dict) and cls._get_type(value) == FUNCTION_TYPE:
                try:
                    function = cls.convert_back(value)
                except ValueError:
                    closure = cls._get_data(value)['closure']
                    cls._get_data(closure).append(cls._make_cell(decoded_class))
                    function = cls.convert_back(value)
                function.__globals__.update({decoded_class.__name__: decoded_class})
                if value.get('is_method'):
                    function = MethodType(function, decoded_class)

                setattr(decoded_class, key, function)
        return decoded_class

    @classmethod
    def _convert_iterator(cls, obj):
        data = list(map(cls.convert, obj))
        return cls._create_dict(data, ITERATOR_TYPE)

    @classmethod
    def _convert_back_iterator(cls, obj):
        data = cls._get_data(obj)
        return iter(cls.convert_back(value) for value in data)

    @classmethod
    def _convert_property(cls, obj):
        data = dict(
            fget=cls.convert(obj.fget),
            fset=cls.convert(obj.fset),
            fdel=cls.convert(obj.fdel)
        )
        return cls._create_dict(data, PROPERTY_TYPE)

    @classmethod
    def _convert_back_property(cls, obj):
        data = cls.convert_back(cls._get_data(obj))
        return property(**data)

    # ----------- Helpers -------------

    @staticmethod
    def _create_dict(data, _type, **additional):
        return dict(__type=_type, data=data, **additional)

    @staticmethod
    def _get_type(obj):
        if isinstance(obj, dict):
            return obj.get('__type')

    @staticmethod
    def _get_data(obj):
        if isinstance(obj, dict):
            return obj.get('data')

    @staticmethod
    def _get_methods_father_class(method):
        cls = getattr(
            inspect.getmodule(method),
            method.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
            None
        )
        if isinstance(cls, type):
            return cls

    @staticmethod
    def _make_cell(value):
        return (lambda: value).__closure__[0]

    @staticmethod
    def _is_iterable(obj):
        return hasattr(obj, '__iter__') and hasattr(obj, '__next__') and callable(obj.__iter__)
