
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Curso(Base):
   __tablename__  ='cursos'
   cod_curso = Column(String(20),primary_key=True)
   nombre_curso = Column(String(30), nullable=False)
   creditos = Column(Integer, nullable=False)
   pre_requisitos = Column(String(30), nullable=False)
   
    
    