from enum import Enum

class StatusCode(Enum):
    ACCEPTED = 4
    WRONG_ANSWER = 5
    RUNTIME_ERROR = 6
    TIME_LIMIT_EXCEEDED = 7
    MEMORY_LIMIT_EXCEEDED = 8
    OUTPUT_LIMIT_EXCEEDED = 9
    RESTRICTED_CALL = 10