from model import Person
from json import loads, dumps


class PersonDal:
    @classmethod
    def save(cls, person: Person):
        with open('pessoa.txt', 'a') as arq:
            arq.write(dumps(person.cpf) + ' ')

    @classmethod
    def check(cls):
        cpfs = []
        with open('pessoa.txt', 'r') as arq:
            lines = arq.read()

        for line in lines.split():
            cpfs.append(loads(line))
        return Person(cpfs)
