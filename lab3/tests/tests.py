from unittest import TestCase
from lab3.serializer.serializer import Serializer
from lab3.serializer.constants import JSON_TYPE, XML_TYPE


json_serializer = Serializer.create_serializer(JSON_TYPE)
xml_serializer = Serializer.create_serializer(XML_TYPE)


class TestPrimitives(TestCase):
    def test_nums(self):
        a = -367
        b = 3.93335

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
        string = 'Some string'

        json_converted = json_serializer.dumps(string)
        xml_converted = xml_serializer.dumps(string)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(string, json_converted_back, xml_converted_back)

    def test_bytes(self):
        bytes_value = bytes(4)

        json_converted = json_serializer.dumps(bytes_value)
        xml_converted = xml_serializer.dumps(bytes_value)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(bytes_value, json_converted_back, xml_converted_back)

    def test_bool(self):
        tr = True
        fl = False

        json_converted_t = json_serializer.dumps(tr)
        xml_converted_t = xml_serializer.dumps(tr)

        json_converted_f = json_serializer.dumps(fl)
        xml_converted_f = xml_serializer.dumps(fl)

        json_converted_back_t = json_serializer.loads(json_converted_t)
        xml_converted_back_t = xml_serializer.loads(xml_converted_t)

        json_converted_back_f = json_serializer.loads(json_converted_f)
        xml_converted_back_f = xml_serializer.loads(xml_converted_f)

        return self.assertEqual(tr, json_converted_back_t, xml_converted_back_t) \
            and self.assertEqual(fl, json_converted_back_f, xml_converted_back_f)

    def test_none(self):
        a = None

        json_converted = json_serializer.dumps(a)
        xml_converted = xml_serializer.dumps(a)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(a, json_converted_back, xml_converted_back)


class TestCollections(TestCase):
    def test_list(self):
        lst = [4, 5, 6]

        json_converted = json_serializer.dumps(lst)
        xml_converted = xml_serializer.dumps(lst)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(lst, json_converted_back, xml_converted_back)

    def test_set(self):
        st = {5, 6, 7}

        json_converted = json_serializer.dumps(st)
        xml_converted = xml_serializer.dumps(st)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(st, json_converted_back, xml_converted_back)

    def test_tuple(self):
        tup = (5, 4, 6, 8)

        json_converted = json_serializer.dumps(tup)
        xml_converted = xml_serializer.dumps(tup)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(tup, json_converted_back, xml_converted_back)

    def test_dict(self):
        dct = {'me': 'good mark', 'my group mates': 'are ok with labs'}

        json_converted = json_serializer.dumps(dct)
        xml_converted = xml_serializer.dumps(dct)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        return self.assertEqual(dct, json_converted_back, xml_converted_back)


class TestOthers(TestCase):
    def test_generator(self):
        def generator():
            yield 1
            yield 2
            yield 3

        json_converted = json_serializer.dumps(generator)
        xml_converted = xml_serializer.dumps(generator)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        result = [1, 2, 3]
        json_result = list(json_converted_back())
        xml_result = list(xml_converted_back())

        return self.assertEqual(result, json_result, xml_result)

    def test_iterator(self):
        iterator = iter([1, 2, 3])

        json_converted = json_serializer.dumps(iterator)
        xml_converted = xml_serializer.dumps(iterator)

        json_converted_back = json_serializer.loads(json_converted)
        xml_converted_back = xml_serializer.loads(xml_converted)

        result = [1, 2, 3]
        json_result = list(json_converted_back)
        xml_result = list(xml_converted_back)

        return self.assertEqual(result, json_result)
