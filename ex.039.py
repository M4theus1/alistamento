from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de seu nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar nesse ano corrente.')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, falta(m) {} ano(s) para seu alistamento. '.format(saldo))
elif idade > 18:
    deve = idade - 18
    print('Você já deveria ter se alistado há {} anos. '
          'Compareça a junta militar mais próxima para analisar sua situação. '.format(deve))
