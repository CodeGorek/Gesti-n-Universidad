
from sqlalchemy import Column, Integer, String,Date,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Estudiante(Base):
   __tablename__  ='estudiantes'
   matricula_estudiante = Column(Integer,primary_key=True)
   nombre_estudiante = Column(String(100), nullable=False)
   correo_estudiante = Column(String(40), nullable=False)
   direccion_estudiante = Column(String(30), nullable=False)
   fecha_nacimiento = Column(Date, nullable=False)
   habilitado = Column(Boolean, nullable= False)
   