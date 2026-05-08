from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.calculation import Calculation
from app.schemas.report import CalculationReport

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/calculations", response_model=CalculationReport)
def get_calculation_report(db: Session = Depends(get_db)):
    calculations = db.query(Calculation).all()

    total = len(calculations)

    if total == 0:
        return {
            "total_calculations": 0,
            "operation_counts": {
                "Add": 0,
                "Sub": 0,
                "Multiply": 0,
                "Divide": 0
            },
            "average_result": 0,
            "highest_result": 0,
            "lowest_result": 0,
            "recent_calculations": []
        }

    operation_counts = {
        "Add": 0,
        "Sub": 0,
        "Multiply": 0,
        "Divide": 0
    }

    results = []

    for calculation in calculations:
        operation_counts[calculation.type] = operation_counts.get(calculation.type, 0) + 1
        results.append(calculation.result)

    recent_calculations = (
        db.query(Calculation)
        .order_by(Calculation.id.desc())
        .limit(5)
        .all()
    )

    return {
        "total_calculations": total,
        "operation_counts": operation_counts,
        "average_result": sum(results) / total,
        "highest_result": max(results),
        "lowest_result": min(results),
        "recent_calculations": recent_calculations
    }
