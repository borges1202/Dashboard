nd = {}
for i in range(2):
    print ('-'*10)
    nome = input('nome:')
    idade = input ('idade:')
    nd[nome] = idade
print (f'o nome da pessoa com maior idade é {max(nd, key=nd.get)} com a idade de {max(nd.values())}')