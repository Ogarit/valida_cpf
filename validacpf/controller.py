from model import Person
from dal import PersonDal


class PersonController:
    @classmethod
    def analyze(cls, cpf):
        cpf_default = cpf.replace('.', '').replace('-', '')
        digit = [i * int(d) for p, d in enumerate(cpf_default) for i in range(1, 10) if p + 1 == i]

        if sum(digit) % 11 == int(cpf_default[9]) or sum(digit) % 11 == 10 and int(cpf_default[9]) == 0:
            digit = [i * int(d) for p, d in enumerate(cpf_default) for i in range(0, 10) if p == i]

            if sum(digit) % 11 == int(cpf_default[10]) or sum(digit) % 11 == 10 and int(cpf_default[10]) == 0:
                PersonDal.save(Person(cpf))
                return True
            else:
                return False
        else:
            return False
