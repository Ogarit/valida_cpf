from model import Person


class PersonDal:
    @classmethod
    def save(cls, person: Person):
        with open('pessoa.txt', 'a') as arq:
            arq.write(person.cpf + ' ')

    @classmethod
    def check(cls):
        cpfs = []
        with open('pessoa.txt', 'r') as arq:
            lines = arq.read()

        for line in lines.split():
            cpfs.append(line)
        return Person(cpfs)
