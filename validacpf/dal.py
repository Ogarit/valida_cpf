from model import Person, Cpf
from json import loads, dumps
from connection import Session


class PersonDal:
    @classmethod
    def save(cls, person: Person):
        session = Session()

        new_cpf = Cpf(cpf=dumps(person.cpf))

        session.add(new_cpf)
        session.commit()
        session.close()

    @classmethod
    def check(cls):
        session = Session()
        cpfs = session.query(Cpf).all()

        cpfs = list(map(lambda x: loads(x.cpf), cpfs))

        return Person(cpfs)
