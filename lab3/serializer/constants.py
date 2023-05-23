import types


JSON_TYPE = 'json'
XML_TYPE = 'xml'

PRIMITIVE_TYPES = (int, str, bool, float, type(None))

BYTES_TYPE = 'bytes'
TUPLE_TYPE = 'tuple'
SET_TYPE = 'set'
ITERATOR_TYPE = 'iterator'
CODE_TYPE = 'code'
OBJ_TYPE = 'obj'
MODULE_TYPE = 'module'
CELL_TYPE = 'cell'
FUNCTION_TYPE = 'function'
CLASS_TYPE = 'class'
PROPERTY_TYPE = 'property'

SPACES = (' ', '\n', '\t')

UNSERIALIZABLE_CODE_TYPES = (
    'co_positions',
    'co_lines',
    'co_exceptiontable',
    'co_lnotab',
)

UNSERIALIZABLE_DUNDER = (
    '__mro__',
    '__base__',
    '__basicsize__',
    '__class__',
    '__dictoffset__',
    '__name__',
    '__qualname__',
    '__text_signature__',
    '__itemsize__',
    '__flags__',
    '__weakrefoffset__',
    '__objclass__',
    '__doc__'
)

UNSERIALIZABLE_TYPES = (
    types.WrapperDescriptorType,
    types.MethodDescriptorType,
    types.BuiltinFunctionType,
    types.MappingProxyType,
    types.GetSetDescriptorType,
)
