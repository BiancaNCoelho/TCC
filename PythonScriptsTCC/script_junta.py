import pandas as pd
import os

file = os.path.abspath("input")

arquivos = []

with open(file, 'r') as file:
    for line in file:
        arquivos.append(line.strip())

n = len(arquivos)

print("Lines from the file: ", arquivos, "Array size: ", n)

dataframes = []

# Iterando sobre os arquivos CSV
for caminho_arquivo in arquivos:
        # Lendo o arquivo CSV e adicionando ao DataFrame
        df = pd.read_csv(caminho_arquivo)
        dataframes.append(df)
    
# Concatenando todos os DataFrames em um único DataFrame
df_final = pd.concat(dataframes, ignore_index=True)
data_junto = os.path.abspath("output.csv")
df_final.to_csv(data_junto, index=False)
