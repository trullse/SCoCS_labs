from lab3.serializer.converter import Converter
from lab3.serializer.constants import \
    TRUE, \
    FALSE, \
    NULL


class SerializerXml:
    _converter = Converter()

    @classmethod
    def dumps(cls, obj):
        return cls._convert_to_xml(cls._converter.convert(obj))

    @classmethod
    def dump(cls, obj, file):
        file.write(cls.dumps(obj))

    @classmethod
    def loads(cls, obj):
        result, _ = cls._convert_back_from_xaml(obj)
        return cls._converter.deconvert(result)

    @classmethod
    def load(cls, file):
        return cls.loads(file.read())

    @classmethod
    def _convert_to_xml(cls, obj):
        if isinstance(obj, (bool, int, float, str, type(None))):
            obj_type = type(obj).__name__
            return f'<{obj_type}>{str(obj)}</{obj_type}>'
        elif isinstance(obj, list):
            return f"<list>{''.join(list(map(cls.dumps, obj)))}</list>"
        elif isinstance(obj, dict):
            data = ''.join(
                [f'<{key}>{cls.dumps(value)}</{key}>' for (key, value) in obj.items()]
            )
            return f'<dict>{data}</dict>'
        raise Exception(f'Type {type(obj).__name__} conversion is not available')

    @classmethod
    def _convert_back_from_xaml(cls, obj, pos=0):
        if obj[pos] != '<':
            raise Exception(f'File is broken')

        type_start_pos = type_end_pos = pos + 1
        while obj[type_end_pos] != '>':
            type_end_pos += 1

        obj_type = obj[type_start_pos:type_end_pos]
        method_name = f'_convert_back_{obj_type}'

        if not hasattr(cls, method_name):
            raise Exception(f'Type {obj_type} back conversion is not available')

        return getattr(cls, method_name)(obj, type_end_pos + 1)

    @classmethod
    def _convert_back_str(cls, obj, pos):
        close_tag = '</str>'
        end_pos = cls._get_value(obj, pos, close_tag)

        return obj[pos:end_pos], end_pos + len(close_tag)

    @classmethod
    def _convert_back_bool(cls, obj, pos):
        close_tag = '</bool>'
        end_pos = cls._get_value(obj, pos, close_tag)

        bool_obj = obj[pos:end_pos]

        if bool_obj == TRUE.capitalize():
            return True, end_pos + len(close_tag)
        else:
            return False, end_pos + len(close_tag)

    @classmethod
    def _convert_back_int(cls, obj, pos):
        close_tag = '</int>'
        end_pos = cls._get_value(obj, pos, close_tag)

        int_obj = obj[pos:end_pos]
        return int(int_obj), end_pos + len(close_tag)

    @classmethod
    def _convert_back_float(cls, obj, pos):
        close_tag = '</float>'
        end_pos = cls._get_value(obj, pos, close_tag)

        float_obj = obj[pos:end_pos]
        return float(float_obj), end_pos + len(close_tag)

    @classmethod
    def _convert_back_NoneType(cls, obj, pos):
        close_tag = '</NoneType>'
        end_pos = cls._get_value(obj, pos, close_tag)

        return None, end_pos + len(close_tag)

    @classmethod
    def _convert_back_list(cls, obj, pos):
        end_pos = pos
        open_tag = '<list>'
        close_tag = '</list>'
        deep = 1
        while deep != 0:
            if obj[end_pos:end_pos + len(open_tag)] == open_tag:
                deep += 1
            if obj[end_pos:end_pos + len(close_tag)] == close_tag:
                deep -= 1

            if deep != 0:
                end_pos += 1

        arr = []
        while pos < end_pos:
            result, pos = cls._convert_back_from_xaml(obj, pos)
            arr.append(result)

        return arr, end_pos + len(close_tag)

    @classmethod
    def _convert_back_dict(cls, obj, pos):
        end_pos = pos
        open_tag = '<dict>'
        close_tag = '</dict>'
        deep = 1
        while deep != 0:
            if obj[end_pos:end_pos + len(open_tag)] == open_tag:
                deep += 1
            if obj[end_pos:end_pos + len(close_tag)] == close_tag:
                deep -= 1

            if deep != 0:
                end_pos += 1

        result = {}

        while pos < end_pos:
            key_start_pos = key_end_pos = pos + 1

            while obj[key_end_pos] != '>':
                key_end_pos += 1

            key = obj[key_start_pos:key_end_pos]

            value, pos = cls._convert_back_from_xaml(obj, key_end_pos + 1)
            pos += len(key) + 3

            result[key] = value

        return result, end_pos + len(close_tag)

    @staticmethod
    def _get_value(obj, pos, close_tag):
        end_pos = pos
        while obj[end_pos:end_pos + len(close_tag)] != close_tag:
            end_pos += 1
        return end_pos

