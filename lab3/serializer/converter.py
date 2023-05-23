import base64
import builtins

from lab3.serializer.constants import PRIMITIVE_TYPES, BYTES_TYPE, TUPLE_TYPE, SET_TYPE


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

        else:
            raise Exception("Not implemented")

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
        raise Exception('This type back conversion is not implemented')

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
