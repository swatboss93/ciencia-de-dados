from datetime import datetime
from dateutil.relativedelta import relativedelta

nome = input("Informe seu nome: ")
idade = input("Informe data de nascimento (dd/mm/aaaa): ")

nascimento = datetime.strptime(idade, '%d/%m/%Y').date()

data_centenario = nascimento + relativedelta(years=100)

print(nome + " você ira fazer 100 anos em: " + data_centenario.strftime("%d/%m/%Y"))