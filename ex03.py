import pandas as pd
import numpy as np

arquivo = 'dados_ex03\dados.json'
tabela = pd.read_json(arquivo)

# Alterando todos os 0 para nan
tabela = tabela.replace(0, np.nan)

# Removendo os valores nulos das linhas
tabela = tabela.dropna(axis=0)

# Extraindo indices do menor valor e maior valor
id_min = tabela['valor'].idxmin()
id_max = tabela['valor'].idxmax()

# Extraindo menor e maior valor com base no indice e seus dias referentes
menor_valor_faturamento = tabela.loc[id_min, 'valor']
dia_menor_valor_faturamento = tabela.loc[id_min, 'dia']

maior_valor_faturamento = tabela.loc[id_max, 'valor']
dia_maior_valor_faturamento = tabela.loc[id_max, 'dia']

# Extraindo media dos valores
media_valor = tabela['valor'].mean()

# Primeiro argumento pega total de linhas que sao maiores que a media
# Segundo argumento conta quantidade de linhas
quantidade_valores_maiores_media = tabela[tabela['valor'] > media_valor]['valor'].count()

print(tabela)
print(f"""
Resultados:

• O menor valor de faturamento ocorrido em um dia do mês; 
\033[0:32:40m Resposta: foi {menor_valor_faturamento:.4f} referente ao dia {dia_menor_valor_faturamento} \033[m

• O maior valor de faturamento ocorrido em um dia do mês; 
\033[0:32:40m Resposta: foi {maior_valor_faturamento:.4f} referente ao dia {dia_maior_valor_faturamento} \033[m

• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
\033[0:32:40m Resposta: {quantidade_valores_maiores_media} dias \033[m
""")

