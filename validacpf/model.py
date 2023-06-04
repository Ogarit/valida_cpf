from connection import Base
from sqlalchemy import Column, Integer, String


class Person:
    def __init__(self, cpf):
        self.cpf = cpf


class Cpf(Base):
    __tablename__ = 'cpfs'
    id = Column(Integer, primary_key=True)
    cpf = Column(String(13))
