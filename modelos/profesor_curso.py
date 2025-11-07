from sqlalchemy import Column, Integer,String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class ProfesorCurso(Base):
   __tablename__  ='profesor_curso'
   cod_profesor_curso = Column(Integer,primary_key=True)
   cod_profesor = Column(Integer, nullable=False)
   cod_curso = Column(String(20), nullable=False)
   habilitado = Column(Boolean, nullable=False)
    
    