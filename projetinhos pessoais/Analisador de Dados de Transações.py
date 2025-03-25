import re
import sys
from datetime import date
#informações do cliente

saldo_atual = float(input('Qual o saldo atual da conta R$'))
deposito_ou_retirada = input('digite [1] para um deposito ou [2] para uma retirada:').lower()
valor = float(input('Digite o valor da transação R$'))
data = date.today()
desc = str(input('Descrição da transação:'))
print ('\n')

#calculos de depósitos e retiradas

if deposito_ou_retirada == '2' and valor > saldo_atual:
           print ('saldo insuficiente')
elif deposito_ou_retirada == '2':
    print (f'A retirada é de R${valor}')
    print (f'O saldo atual é R${saldo_atual-valor}')
    print (f'A data da transação é {data}')
    print (f'A descrição da transação é:{desc}')   
elif deposito_ou_retirada == '1':
       print (f'O deposito será de R${valor}')
       print (f'O saldo atual é R${saldo_atual+valor}')
       print (f'A data da transação é {data}')
       print (f'A descrição da transação é: {desc}')