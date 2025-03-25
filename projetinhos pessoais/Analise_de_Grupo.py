#criaçao das listas

nomes = {}
sexos = {}
cont = 0
media = 0

#pergunto quantas pessoas vai ter no grupo

P=int(input('quantas pessoas no grupo?'))

for x in range(1,P+1):
    #começo a pegar as informaçoes

    print('-'*5, f'{x}º pessoa', '-'*5)
    nome = input('qual é o seu nome:').lower()
    idade = float(input('qual é sua idade:'))
    sexo = input('qual o seu sexo [M/F]:').lower() 

    #validação de idade
    if idade <= 0:
        print ('Erro: idade inválida. Por favor, informe uma idade maior que 0')
        exit()
    elif idade >= 120:
        print ('Erro: idade inválida. Por favor, informe uma idade menor que 120')
        exit()

    #Esse aqui eu relaciono os nomes com as idades
    nomes[nome] = idade 

    #Começo a organizar as medias e os sexos (tambem faço a validaçao do sexo)
     
    media = idade+media
    media_final = media/P
    if sexo == 'm':
        sexo = 'masculino'
    elif sexo == 'f':
        sexo = 'feminino'
    elif sexo != 'm' or 'f':
        print ('Erro: Sexo inválido.'
        ' Por favor, informar "M" para masculino ou "F" para feminino')
        exit()
    if sexo == 'feminino' and idade < 20:
        cont = cont+1
    sexos[sexo] = idade

 #Aqui todas as informaçoes recolhidas serão mostradas

print (f'A media de idade do grupo com {P} pessoas é {media_final}')
print (f'A pessoa com maior idade do grupo se chama {max(nomes, key=nomes.get)} com a idade de {max(nomes.values())} seu sexo é {max(sexos, key=sexos.get)}.')
print (f'E tem {cont} mulheres com menos de 20 anos')
input ('precione qualquer tecla para sair...')
#informaçoes uteis para mim depois
#max é o maior valor dentro de uma lista
                                    #uma lista sera isso aqui x = {} --> x[y]
#max(nomes, key=nomes.get) será utilizado para descobrir o nome com a maior idade, já max(nomes.values()) seria utilizado para descobrir a maior idade
