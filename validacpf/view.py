from controller import PersonController as Controll
from dal import PersonDal

while True:
    try:
        value = input('Insira um cpf [Digite H/h para ver o historico ou S/s para Sair]: ')
        if value.lower() == 's':
            break
        elif value.lower() == 'h':
            cpfs = PersonDal.check().cpf
            for cpf in cpfs:
                print(cpf)
            break
        else:
            if Controll.analyze(value):
                print('O cpf é valido')
            else:
                print('O cpf não é valido')
    except IndexError:
        print('O cpf é formado por 11 números!')

print(f'{"-" * 3}Finalizado{"-" * 3}')
