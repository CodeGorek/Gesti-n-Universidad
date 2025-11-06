from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Carrera(Base):
   __tablename__  ='carreras'
   cod_carrera = Column(String(30),primary_key=True)
   nombre_carrera = Column(String(200), nullable=False)
   creditos_max_semestre = Column(Integer, nullable=False)
   semestre_duracion = Column(Integer, nullable=False)
   habilitado = Column(Boolean, nullable=False)