from pydantic import BaseModel, field_validator
from typing import Literal


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: Literal["Add", "Sub", "Multiply", "Divide"]

    @field_validator("b")
    @classmethod
    def check_divide_by_zero(cls, value, info):
        if info.data.get("type") == "Divide" and value == 0:
            raise ValueError("Cannot divide by zero")
        return value


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: float

    class Config:
        from_attributes = True
