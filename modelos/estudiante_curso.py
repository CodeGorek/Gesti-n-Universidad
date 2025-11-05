from sqlalchemy import Column, Integer,String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Estudiante_Curso(Base):
   __tablename__  ='estudiante_curso'
   cod_estudiante_curso = Column(Integer,primary_key=True)
   matricula_estudiante = Column(Integer, nullable=False)
   cod_curso = Column(String(20), nullable=False)
   habilitado = Column(Boolean, nullable=False)