from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Profesor(Base):
   __tablename__  ='profesores'
   cod_profesor = Column(Integer,primary_key=True)
   nombre_profesor = Column(String(30), nullable=False)
   correo_profesor = Column(String(30), nullable=False)
   especialidad = Column(String(30), nullable=False)
   habilitado = Column(Boolean, nullable=False)