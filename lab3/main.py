import math

from serializer.serializer import Serializer
from serializer.converter import Converter
from serializer.constants import JSON_TYPE, XML_TYPE
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


class PropertyClass:
    calls = 0

    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        self.calls += 1
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self.calls += 1
        self._temperature = value


class PrimitiveTypesCheck(TestCase):
    def test_nums(self):
        json_serializer = Serializer.create_serializer(JSON_TYPE)
        xml_serializer = Serializer.create_serializer(XML_TYPE)

        a = -324
        b = 3.93493

        json_converted_a = json_serializer.dumps(a)
        json_converted_b = json_serializer.dumps(b)

        xml_converted_a = xml_serializer.dumps(a)
        xml_converted_b = xml_serializer.dumps(b)

        json_converted_back_a = json_serializer.loads(json_converted_a)
        json_converted_back_b = json_serializer.loads(json_converted_b)

        xml_converted_back_a = xml_serializer.loads(xml_converted_a)
        xml_converted_back_b = xml_serializer.loads(xml_converted_b)

        return self.assertEqual(a, json_converted_back_a, xml_converted_back_a) \
            and self.assertEqual(b, json_converted_back_b, xml_converted_back_b)

    def test_string(self):
        json_serializer = Serializer.create_serializer(JSON_TYPE)
        xml_serializer = Serializer.create_serializer(XML_TYPE)

        string = 'Some string'

        json_converted = json_serializer.dumps(string)
        xml_converted = xml_serializer.dumps(string)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(string, json_converted_back, xml_converted_back)

    def test_list(self):
        # json_serializer = Serializer.create_serializer('json')

        list_ = [5, 6, 7]
        converted = Converter.convert(list_)
        list_back = Converter.convert_back(converted)

        return self.assertEqual(list_, list_back)

    def test_collections(self):
        json_serializer = Serializer.create_serializer(JSON_TYPE)

        sett = {5, 6, 7}
        tuplee = (4, 6)
        converted_set = json_serializer.dumps(sett)
        set_back = json_serializer.loads(converted_set)
        converted_tuple = json_serializer.dumps(tuplee)
        tuple_back = json_serializer.loads(converted_tuple)

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
        json_serializer = Serializer.create_serializer(JSON_TYPE)
        xml_serializer = Serializer.create_serializer(XML_TYPE)

        json_converted_class = json_serializer.dumps(Class2)
        xml_converted_class = xml_serializer.dumps(Class2)

        json_class_back = json_serializer.loads(json_converted_class)
        xml_class_back = xml_serializer.loads(xml_converted_class)

        return self.assertEqual(Class2.a, json_class_back.a, xml_class_back) \
            and self.assertEqual(Class2.b, json_class_back.b, xml_class_back)

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

    def test_property(self):
        converted_class = Converter.convert(PropertyClass)
        class_back = Converter.convert_back(converted_class)

        source = PropertyClass()
        converted = class_back()

        source.temperature = 5
        temp = source.temperature

        converted.temperature = 5
        temp = converted.temperature

        return self.assertEqual(source.calls, converted.calls)


if __name__ == '__main__':
    main()
