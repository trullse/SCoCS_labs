from constants import PRIMITIVE_TYPES


class Converter:
    @classmethod
    def convert(cls, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj
        else:
            raise Exception("Not implemented")

    @classmethod
    def convert_back(cls, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj
