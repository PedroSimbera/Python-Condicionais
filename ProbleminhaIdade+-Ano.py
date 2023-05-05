import datetime
anoNascimento: int(input("Qual seu ano de nascimento: "))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento
if (idade>18):
    print("Maior de idade, você tem", idade)
else:
    print("Menor de idade, você tem", idade)