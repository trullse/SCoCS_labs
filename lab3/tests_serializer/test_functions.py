import unittest
import math

from serializer_leonenko.serializer import Serializer

JSON_DATATYPE = 'json'
XML_DATATYPE = 'xml'
GLOBAL_VALUE = 19

json_serializer = Serializer.create_serializer(JSON_DATATYPE)
xml_serializer = Serializer.create_serializer(XML_DATATYPE)


def simple_func():
    return 17


def recursion_func(x):
    if x < 2:
        return 1
    return recursion_func(x - 1) * x


def divide_func(x):
    return x // (x - 2)


def sqrt_func(x):
    return math.sqrt(x)


def other_function():
    return simple_func()


def func_with_global():
    return GLOBAL_VALUE * 2


def decorator(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        return value / 3 + 32

    return wrapper


@decorator
def decorated():
    return 22 + 1


lambda_function = lambda x: (x ** x) // 3


def top_function():
    val = 32

    def closure():
        nonlocal val
        val += 1
        return val
    return closure


class TestFunctions(unittest.TestCase):
    def test_simple_function(self):
        json_dumped = json_serializer.dumps(simple_func)
        json_decoded = json_serializer.loads(json_dumped)
        xml_dumped = xml_serializer.dumps(simple_func)
        xml_decoded = xml_serializer.loads(xml_dumped)

        result = simple_func()
        json_result = json_decoded()
        xml_result = xml_decoded()

        return self.assertEqual(result, json_result, xml_result)

    def test_func_with_params(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(divide_func))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(divide_func))

        x = 21
        result = divide_func(x)
        json_result = json_decoded(x)
        xml_result = xml_decoded(x)

        return self.assertEqual(result, json_result, xml_result)

    def test_func_with_lib(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(sqrt_func))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(sqrt_func))

        x = 5
        result = sqrt_func(x)
        json_result = json_decoded(x)
        xml_result = xml_decoded(x)

        return self.assertEqual(result, json_result, xml_result)

    def test_recursion_func(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(recursion_func))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(recursion_func))

        x = 33
        result = recursion_func(x)
        json_result = json_decoded(x)
        xml_result = xml_decoded(x)

        return self.assertEqual(result, json_result, xml_result)

    def test_lambda(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(lambda_function))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(lambda_function))

        x = 21
        result = lambda_function(x)
        json_result = json_decoded(x)
        xml_result = xml_decoded(x)

        return self.assertEqual(result, json_result, xml_result)

    def test_other_function(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(other_function))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(other_function))

        result = other_function()
        json_result = json_decoded()
        xml_result = xml_decoded()

        return self.assertEqual(result, json_result, xml_result)

    def test_func_with_global_value(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(func_with_global))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(func_with_global))

        result = func_with_global()
        json_result = json_decoded()
        xml_result = xml_decoded()

        return self.assertEqual(result, json_result, xml_result)


class TestFunctionWrappers(unittest.TestCase):
    def test_decorator(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(decorator))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(decorator))

        @json_decoded
        def json_func():
            return 22+1

        @xml_decoded
        def xml_func():
            return 22+1

        result = decorated()
        json_result = json_func()
        xml_result = xml_func()

        return self.assertEqual(result, json_result, xml_result)

    def test_decorated_func(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(decorated))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(decorated))

        result = decorated()
        json_result = json_decoded()
        xml_result = xml_decoded()

        return self.assertEqual(result, json_result, xml_result)


class TestClosure(unittest.TestCase):
    def test_closure_function(self):
        closure = top_function()
        json_decoded = json_serializer.loads(json_serializer.dumps(closure))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(closure))

        result = 33
        json_result = json_decoded()
        xml_result = xml_decoded()

        self.assertEqual(result, json_result, xml_result)

        result = 34
        json_result = json_decoded()
        xml_result = xml_decoded()

        return self.assertEqual(result, json_result, xml_result)
