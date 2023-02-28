import pandas as pd

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53}

# Cria um DataFrame a partir do dicionário
tabela = pd.DataFrame(faturamento.items(), columns=['Estado', 'Faturamento'])

# Calcula o valor total do faturamento
valor_total = tabela['Faturamento'].sum()

# Calcula o percentual de representação de cada estado
tabela['% Representação'] = tabela['Faturamento'] / valor_total * 100

# Imprime a Tabela com o percentual de representação de cada estado
print(tabela)
