from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuração de URL para MySQL, assumindo que o banco de dados MySQL está rodando localmente
DATABASE_URL = "mysql+pymysql://root:root@localhost/login_api"

# Criação do engine para o SQLAlchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definição dos modelos
Base = declarative_base()

# Dependência para obter sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
