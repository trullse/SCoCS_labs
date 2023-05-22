from serializer.serializer import Serializer
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


if __name__ == '__main__':
    main()
