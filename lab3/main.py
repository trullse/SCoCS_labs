from serializer.serializer import Serializer
from serializer.converter import Converter
from unittest import TestCase, main


class PrimitiveTypesCheck(TestCase):
    def test_nums(self):
        json_serializer = Serializer.create_serializer('json')
        # xml_serializer = Serializer.create_serializer('xml')

        a = -324
        b = 3.93493

        json_converted_a = json_serializer.dumps(a)
        json_converted_b = json_serializer.dumps(b)

        # xml_converted_a = xml_serializer.dumps(a)
        # xml_converted_b = xml_serializer.dumps(b)

        json_converted_back_a = json_serializer.loads(json_converted_a)
        json_converted_back_b = json_serializer.loads(json_converted_b)

        # xml_converted_back_a = xml_serializer.loads(xml_converted_a)
        # xml_converted_back_b = xml_serializer.loads(xml_converted_b)

        # return self.assertEqual(a, json_converted_back_a, xml_converted_back_a) \
        #     and self.assertEqual(b, json_converted_back_b, xml_converted_back_b)

        return self.assertEqual(a, json_converted_back_a) \
            and self.assertEqual(b, json_converted_back_b)

    def test_list(self):
        # json_serializer = Serializer.create_serializer('json')

        list_ = [5, 6, 7]
        converted = Converter.convert(list_)
        list_back = Converter.convert_back(converted)

        return self.assertEqual(list_, list_back)

    def test_collections(self):
        # json_serializer = Serializer.create_serializer('json')

        sett = {5, 6, 7}
        tuplee = (4, 6)
        converted_set = Converter.convert(sett)
        set_back = Converter.convert_back(converted_set)
        converted_tuple = Converter.convert(tuplee)
        tuple_back = Converter.convert_back(converted_tuple)

        return self.assertEqual(sett, set_back) and self.assertEqual(tuplee, tuple_back)


if __name__ == '__main__':
    main()
