import unittest

from lab3.serializer.serializer import Serializer
JSON_DATATYPE = 'json'
XML_DATATYPE = 'xml'

json_serializer = Serializer.create_serializer(JSON_DATATYPE)
xml_serializer = Serializer.create_serializer(XML_DATATYPE)


class ValueClass:
    a = 1


class ClassWithStaticAndClassMethods:
    b = 32131

    @staticmethod
    def static_method():
        return 5

    @classmethod
    def class_method(cls):
        return cls.b


class Class1:
    def __init__(self):
        super().__init__()
        self.a = 1

    def method1(self):
        return self.a


class Class2:
    def __init__(self):
        super().__init__()
        self.b = 31

    def method2(self):
        return self.b


class Class3(Class1, Class2):
    def __init__(self):
        super().__init__()


class Class4:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        self._temperature = value


class TestPropertyClass(unittest.TestCase):
    def test_property(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(Class4))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(Class4))

        original = json_decoded(5)
        original.temperature = 10
        temp = original.temperature


class TestSimpleClass(unittest.TestCase):
    def test_class_with_value(self):

        json_decoded = json_serializer.loads(json_serializer.dumps(ValueClass))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(ValueClass))

        result = ValueClass.a
        json_test_result = json_decoded.a
        xml_test_result = xml_decoded.a

        return self.assertEqual(result, json_test_result, xml_test_result)

    def test_class_with_methods(self):

        json_decoded = json_serializer.loads(json_serializer.dumps(ClassWithStaticAndClassMethods))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(ClassWithStaticAndClassMethods))

        result = ClassWithStaticAndClassMethods.static_method()
        json_test_result = json_decoded.static_method()
        xml_test_result = xml_decoded.static_method()

        self.assertEqual(result, json_test_result, xml_test_result)

        result = ClassWithStaticAndClassMethods.class_method()
        json_test_result = json_decoded.class_method()
        xml_test_result = xml_decoded.class_method()

        self.assertEqual(result, json_test_result, xml_test_result)


class TestClassInheritance(unittest.TestCase):
    def test_double_inheritance(self):

        json_decoded = json_serializer.loads(json_serializer.dumps(Class3))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(Class3))

        result = Class3().method1()
        json_result = json_decoded().method1()
        xml_result = xml_decoded().method1()

        self.assertEqual(result, json_result, xml_result)

        result = Class3().method2()
        json_result = json_decoded().method2()
        xml_result = xml_decoded().method2()

        self.assertEqual(result, json_result, xml_result)


class TestInheritanceObjects(unittest.TestCase):
    def test_objects(self):

        json_decoded = json_serializer.loads(json_serializer.dumps(Class3()))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(Class3()))

        result = Class3().method1()
        json_result = json_decoded.method1()
        xml_result = xml_decoded.method1()

        self.assertEqual(result, json_result, xml_result)

        result = Class3().method2()
        json_result = json_decoded.method2()
        xml_result = xml_decoded.method2()

        self.assertEqual(result, json_result, xml_result)


if __name__ == '__main__':
    unittest.main()