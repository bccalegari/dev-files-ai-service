from enum import Enum

from src.app.enterprise.domain.error_code_value import ErrorCodeValue


class ErrorCode(Enum):
    UNAUTHORIZED = ErrorCodeValue("UNAUTHORIZED", 401)
    BAD_REQUEST = ErrorCodeValue("BAD_REQUEST", 400)
    NOT_FOUND = ErrorCodeValue("NOT_FOUND", 404)
    UNPROCESSABLE_ENTITY = ErrorCodeValue("UNPROCESSABLE_ENTITY", 422)
    INTERNAL_SERVER_ERROR = ErrorCodeValue("INTERNAL_SERVER_ERROR", 500)
