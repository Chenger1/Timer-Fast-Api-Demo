from typing import (
    Any,
    Dict,
    Optional
)

from fastapi import (
    HTTPException,
    status
)


class DuplicatedError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None):
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class ValidationError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None):
        super().__init__(status.HTTP_422_UNPROCESSABLE_ENTITY, detail, headers)


class AuthError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, detail, headers)
