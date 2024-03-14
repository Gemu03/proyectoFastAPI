from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://sql10691174:Tl7JJAkI61@sql10.freesqldatabase.com:3306/sql10691174"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def test_connection():
    try:
        # Intenta conectar a la base de datos y ejecutar una consulta simple
        with SessionLocal() as session:
            session.execute(text('SELECT * FROM EMPLEADO'))
        print("La conexión a la base de datos se realizó correctamente.")
    except SQLAlchemyError as e:
        print("Hubo un error al intentar conectarse a la base de datos.")
        print(str(e))

# Llama a la función para probar la conexión
test_connection()

from sqlalchemy.orm import Session
from .base_de_datos import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()