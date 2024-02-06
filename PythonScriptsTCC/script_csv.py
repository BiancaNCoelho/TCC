import pandas as pd
import csv
import os

file = os.path.abspath("input")

arquivos = []

with open(file, 'r') as file:
    for line in file:
        arquivos.append(line.strip())

n = len(arquivos)

print("Lines from the file: ", arquivos, "Array size: ", n)

# Tira linhas duplicadas
for i in range(n):
  data = pd.read_csv(arquivos[i]) #, delimiter=';')
  a = data.drop_duplicates()
  a.to_csv("data_" + str(i) + "_" + arquivos[i], index=False)
