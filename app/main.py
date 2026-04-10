from fastapi import FastAPI
from app.database import Base, engine
from app.api.users import router as users_router
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Secure User App")


@app.get("/")
def read_root():
    return {"message": "FastAPI Secure User App is running"}


app.include_router(users_router)
