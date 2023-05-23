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
