
import pandas

df_dados = pandas.read_csv("dados.csv")

df_dados #datafframe

df_dados.head() #os 5 primeiros

df_dados.info() # informações básicas

#média da coluna numérica chamada idade.
soma = df_dados ["idade"].sum()
media = soma/7
media = (f'{media:.2f}')
print (media)


#valor mínimo e máximo da coluna chamada salario.
min = df_dados ["salario"].min()
max = df_dados ["salario"].max()
print(min)
print(max)


#todos os valores únicos de uma coluna chamada departamento.
valor_unico = df_dados["departamento"].unique()
print (valor_unico)


#idade é maior que 30.
df_dados [df_dados["idade"]> 30]


#filtroS
filtro_vendas = df_dados ["departamento"] == "Vendas"
filtro_rh = df_dados ["departamento"] == "RH"
filtro_ti = df_dados ["departamento"] == "TI"


#Selecionar as colunas nome e salario de todos os funcionários do departamento Vendas.
nome_salario = df_dados.loc[filtro_vendas ,["nome", "salario"]]
print (nome_salario) 


#Crie uma nova coluna chamada bonus que é 10% do valor da coluna salario, Adicione uma coluna chamada salario_total que soma salario e bonus.
df_dados ['bonus'] = df_dados ['salario']*0.1
df_dados ["salario total"] = df_dados ["bonus"] + df_dados ["salario"]
df_dados


#calculo da soma de cada departamento
soma_vendas = df_dados.loc[filtro_vendas ,["salario total"]].sum()
soma_rh =  df_dados.loc[filtro_rh, ["salario total"]].sum()
soma_ti = df_dados.loc[filtro_ti, ["salario total"]].sum()



#media de cada departamento
media_vendas = soma_vendas/3
media_rh = soma_rh/2
media_ti = soma_ti/3

print (media_vendas)
print (media_rh)
print (media_ti)


#Conte o número de funcionários em cada departamento.
df_dados["departamento"].value_counts() 


import matplotlib.pyplot as plt


#grafico de vendas
plt.plot(["vendas", "ti", "rh"], [media_vendas, media_ti, media_rh])
plt.title('media de salario por departamento')
plt.xlabel('')
plt.ylabel('')
plt.show()


idade = df_dados ['idade']
print (idade)


#histograma de idade
plt.hist(idade)
