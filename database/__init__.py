from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ПУть к бд
SQLALCHEMY_DATABASE_URL = 'sqlite:///health.db'
# Двигатель
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Соединение
SessionLocal = sessionmaker(bind=engine)
# Класс для наследования в таюлицах
Base = declarative_base()


from database import models


def get_db():
    db = SessionLocal()

    try:
        yield db

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()