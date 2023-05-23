from lab3.serializer.converter import Converter
from lab3.serializer.constants import \
    SPACES, \
    TRUE, \
    FALSE, \
    NULL


class SerializerJson:
    _converter = Converter()

    @classmethod
    def dump(cls, obj, file):
        file.write(cls.dumps(obj))

    @classmethod
    def dumps(cls, obj):
        return cls._convert_to_json(Converter.convert(obj))

    @classmethod
    def load(cls, file):
        return cls.loads(file.read())

    @classmethod
    def loads(cls, obj):
        result, pos = cls._convert_back_from_json(obj)
        return cls._converter.convert_back(result)

    @classmethod
    def _convert_to_json(cls, obj):
        if isinstance(obj, str):
            return f'"{obj}"'
        elif isinstance(obj, (int, float)):
            return str(obj)
        elif isinstance(obj, bool):
            return str(bool).lower()
        elif isinstance(obj, type(None)):
            return "null"
        elif isinstance(obj, list):
            return f"[{','.join(list(map(cls.dumps, obj)))}]"
        elif isinstance(obj, dict):
            data = ','.join(
                [f'"{key}": {cls.dumps(value)}' for (key, value) in obj.items()]
            )
            return f'{{{data}}}'
        raise Exception(f'{type(obj)} type conversion to json is not implemented')

    @classmethod
    def _convert_back_from_json(cls, obj: str, pos: int = 0):
        cls._ignore_spaces(obj, pos)
        if obj[pos].isdigit() or obj[pos] == '-':
            return cls._convert_back_nums(obj, pos)
        elif obj[pos] == '"':
            return cls._convert_back_string(obj, pos)
        elif obj[pos] in (TRUE[0], FALSE[0]):
            if obj[pos] == TRUE[0]:
                pos += len(TRUE)
                return True, pos
            elif obj[pos] == FALSE[0]:
                pos += len(FALSE)
                return False, pos
        elif obj[pos] == NULL[0]:
            pos += len(NULL)
            return None, pos
        elif obj[pos] == '[':
            return cls._convert_back_list(obj, pos)
        elif obj[pos] == '{':
            return cls._convert_back_dict(obj, pos)
        else:
            raise Exception(f"The type in position {pos} is undefined")

    @classmethod
    def _convert_back_nums(cls, obj, pos):
        start_pos = end_pos = pos
        end_pos += 1  # accounting '-' symbol
        while end_pos < len(obj) and (obj[end_pos].isdigit() or obj[end_pos] == '.'):
            end_pos += 1

        num = obj[start_pos:end_pos]
        if num.count('.'):
            return float(num), end_pos
        else:
            return int(num), end_pos

    @classmethod
    def _convert_back_string(cls, obj, pos):
        start_pos = end_pos = pos + 1
        while obj[end_pos] != '"':
            end_pos += 1

        return obj[start_pos:end_pos], end_pos + 1

    @classmethod
    def _convert_back_list(cls, obj, pos):
        start_pos = end_pos = pos + 1
        braces = 1
        while braces != 0:
            if obj[end_pos] == '[':
                braces += 1
            elif obj[end_pos] == ']':
                braces -= 1

            end_pos += 1

        output_list = []
        while start_pos < end_pos - 2:
            while obj[start_pos] in (' ', ',', '\n', '\t'):
                start_pos += 1
            res, start_pos = cls._convert_back_from_json(obj, start_pos)
            output_list.append(res)

        return output_list, end_pos

    @classmethod
    def _convert_back_dict(cls, obj, pos):
        start_pos = end_pos = pos + 1
        braces = 1
        while braces != 0:
            if obj[end_pos] == '{':
                braces += 1
            elif obj[end_pos] == '}':
                braces -= 1

            end_pos += 1

        output_dict = {}
        while start_pos < end_pos - 2:
            while obj[start_pos] in (' ', ',', '\n', '\t'):
                start_pos += 1
            key, start_pos = cls._convert_back_from_json(obj, start_pos)
            while obj[start_pos] in (' ', ',', '\n', '\t', ':'):
                start_pos += 1
            value, start_pos = cls._convert_back_from_json(obj, start_pos)

            output_dict[key] = value

        return output_dict, end_pos

    @staticmethod
    def _ignore_spaces(obj: str, pos: int):
        while obj[pos] in SPACES:
            pos += 1
        return pos
