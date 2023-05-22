from converter import Converter


class SerializerJson:
    @classmethod
    def dumps(cls, obj):
        return cls._convert_to_json(Converter.convert(obj))

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
