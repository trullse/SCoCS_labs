from lab3.serializer.converter import Converter
from lab3.serializer.constants import SPACES


class SerializerJson:
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
        return result

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

    @staticmethod
    def _ignore_spaces(obj: str, pos: int):
        while obj[pos] in SPACES:
            pos += 1
        return pos
