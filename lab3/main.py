import math

from serializer.serializer import Serializer
from serializer.converter import Converter
from unittest import TestCase, main


def func(x):
    a = 5
    if x > 5:
        return x
    return a


class Class1:
    a = 13


class Class2(Class1):
    b = 14


class Class3(Class2):
    @classmethod
    def sum(cls):
        return cls.a + cls.b


def func_with_module(x):
    return math.sin(x)


iterator = iter([1, 2, 3, 4, 5])


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

    def test_functions(self):
        converted_func = Converter.convert(func)
        func_back = Converter.convert_back(converted_func)

        return self.assertEqual(func_back(8), func(8)) and self.assertEqual(func_back(1), func(1))

    def test_func_with_module(self):
        converted_func = Converter.convert(func_with_module)
        func_back = Converter.convert_back(converted_func)

        return self.assertEqual(func_back(0), func_with_module(0))

    def test_class_simple(self):
        converted_class = Converter.convert(Class1)
        class_back = Converter.convert_back(converted_class)

        return self.assertEqual(Class1.a, class_back.a)

    def test_class_inherited(self):
        converted_class = Converter.convert(Class2)
        class_back = Converter.convert_back(converted_class)

        return self.assertEqual(Class2.a, class_back.a) and self.assertEqual(Class2.b, class_back.b)

    def test_class_with_method(self):
        converted_class = Converter.convert(Class3)
        class_back = Converter.convert_back(converted_class)

        return self.assertEqual(Class3.sum(), class_back.sum())

    def test_iter(self):
        converted_iter = Converter.convert(iterator)
        iterator_back = Converter.convert_back(converted_iter)

        result = [1, 2, 3, 4, 5]
        back_result = list(iterator_back)

        return self.assertEqual(result, back_result)


if __name__ == '__main__':
    main()
