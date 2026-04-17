from app.database import SessionLocal
from app.models.calculation import Calculation
from app.core.calculation_factory import CalculationFactory


def test_insert_calculation_record():
    db = SessionLocal()

    result = CalculationFactory.compute(10, 5, "Add")

    calculation = Calculation(
        a=10,
        b=5,
        type="Add",
        result=result
    )

    db.add(calculation)
    db.commit()
    db.refresh(calculation)

    assert calculation.id is not None
    assert calculation.a == 10
    assert calculation.b == 5
    assert calculation.type == "Add"
    assert calculation.result == 15

    db.close()
