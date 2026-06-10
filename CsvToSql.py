import pandas as pd
from sqlalchemy import create_engine

#Ler o CSV (separado por ;)
df = pd.read_csv('Data/csv_dataset_vendas.csv', sep=';')

#LIMPEZA DOS DADOS

# remover colunas vazias extras 
df = df.iloc[:, :13]

# renomear colunas
df.columns = [
    'data', 'mes', 'ano', 'produto', 'categoria',
    'regiao', 'vendedor', 'quantidade',
    'preco_unitario', 'receita', 'custo', 'lucro', 'margem'
]

# remover "R$ ", pontos de milhar e ajustar decimal
for col in ['preco_unitario', 'receita', 'custo', 'lucro']:
    df[col] = (
        df[col]
        .str.replace('R$', '', regex=False)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .str.strip()
        .astype(float)
    )

# tratar margem (remover % e dividir por 100)
df['margem'] = (
    df['margem']
    .str.replace('%', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float) / 100
)

# converter data
df['data'] = pd.to_datetime(df['data'], dayfirst=True)

#C onectar NO MYSQL
engine = create_engine("mysql+pymysql://root:SENHA@localhost/vendas_db")

# ENVIAR PARA O BANCO
df.to_sql('vendas', engine, if_exists='replace', index=False)

print("✅ Dados carregados com sucesso!")
