from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationRead
from app.core.calculation_factory import CalculationFactory

router = APIRouter(prefix="/calculations", tags=["Calculations"])


@router.post("/", response_model=CalculationRead)
def create_calculation(calculation: CalculationCreate, db: Session = Depends(get_db)):
    result = CalculationFactory.compute(calculation.a, calculation.b, calculation.type)

    new_calculation = Calculation(
        a=calculation.a,
        b=calculation.b,
        type=calculation.type,
        result=result
    )

    db.add(new_calculation)
    db.commit()
    db.refresh(new_calculation)

    return new_calculation


@router.get("/", response_model=list[CalculationRead])
def get_calculations(db: Session = Depends(get_db)):
    return db.query(Calculation).all()


@router.get("/{calculation_id}", response_model=CalculationRead)
def get_calculation(calculation_id: int, db: Session = Depends(get_db)):
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    return calculation


@router.put("/{calculation_id}", response_model=CalculationRead)
def update_calculation(calculation_id: int, updated_data: CalculationCreate, db: Session = Depends(get_db)):
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    calculation.a = updated_data.a
    calculation.b = updated_data.b
    calculation.type = updated_data.type
    calculation.result = CalculationFactory.compute(updated_data.a, updated_data.b, updated_data.type)

    db.commit()
    db.refresh(calculation)

    return calculation


@router.delete("/{calculation_id}")
def delete_calculation(calculation_id: int, db: Session = Depends(get_db)):
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    db.delete(calculation)
    db.commit()

    return {"message": "Calculation deleted successfully"}
