from lab3.serializer.constants import JSON_TYPE, XML_TYPE
from lab3.serializer.serializer_json import SerializerJson
from lab3.serializer.serializer_xml import SerializerXml


class Serializer:
    @staticmethod
    def create_serializer(stype):
        if stype == JSON_TYPE:
            return SerializerJson()
        elif stype == XML_TYPE:
            return SerializerXml
        else:
            raise Exception("Unresolved serializer type")
