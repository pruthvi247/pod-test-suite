
import enum


class ColumnHeaders(enum.Enum):

        ID = 1
        TEST_CASE = 2
        METHOD = 3
        URL = 4
        API_INPUT = 5
        EXPECTED_OUTPUT = 6
        EXPECTED_STATUS_CODE = 7
        NOTES = 8

class RestMethods(enum.Enum):

        POST = 1
        GET = 2
        PUT = 3
        DELETE = 4


