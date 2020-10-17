
import enum


class ColumnHeaders(enum.Enum):

        ID = 1
        TEST_CASE = 2
        METHOD = 3
        URL = 4
        API_INPUT = 5
        DEPENDENT =6
        EXPECTED_OUTPUT = 7
        EXPECTED_STATUS_CODE = 8
        NOTES = 9

class RestMethods(enum.Enum):

        POST = 1
        GET = 2
        PUT = 3
        DELETE = 4




