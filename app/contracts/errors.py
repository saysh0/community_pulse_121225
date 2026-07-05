from pydantic import BaseModel


class ErrorIem(BaseModel):
    field: str
    message: str


class ErrorResponse(BaseModel):
    error: str
    details: list[ErrorIem] = []