from pydantic import BaseModel
from typing import Dict, List
from app.schemas.calculation import CalculationRead


class CalculationReport(BaseModel):
    total_calculations: int
    operation_counts: Dict[str, int]
    average_result: float
    highest_result: float
    lowest_result: float
    recent_calculations: List[CalculationRead]
