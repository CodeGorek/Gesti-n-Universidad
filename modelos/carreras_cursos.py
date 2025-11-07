from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class CarreraCursos(Base):
   __tablename__  ='carrera_cursos'
   cod_carrera_curso = Column(Integer,primary_key=True)
   cod_curso = Column(String(20), nullable=False)
   cod_carrera = Column(String(30), nullable=False)
   habilitado = Column(Boolean, nullable=False)