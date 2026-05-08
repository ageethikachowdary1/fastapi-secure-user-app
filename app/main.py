from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.api.users import router as users_router
from app.api.calculations import router as calculations_router
from app.api.auth import router as auth_router
from app.api.reports import router as reports_router
from app.models.user import User
from app.models.calculation import Calculation

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Secure User App")


@app.get("/")
def read_root():
    return {"message": "FastAPI Secure User App is running"}


# include routers
app.include_router(users_router)
app.include_router(calculations_router)
app.include_router(auth_router)
app.include_router(reports_router)

# serve frontend
app.mount("/static", StaticFiles(directory="app/static"), name="static")
