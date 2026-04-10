from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
import time

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/fastapi_db"
)

engine = None

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("Database connected successfully")
        break
    except Exception:
        print("Database not ready, retrying...")
        time.sleep(2)

if engine is None:
    raise RuntimeError("Could not connect to database")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
