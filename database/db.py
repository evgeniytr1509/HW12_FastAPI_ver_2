from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@195.201.150.230:5433/evgeniy_rt_fa" #
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Определение Base
Base = declarative_base()

# Создаем базу данных, если она не существует
#Base.metadata.create_all(bind=engine)

# Функция для получения сессии базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()