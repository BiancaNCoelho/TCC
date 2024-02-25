import pandas as pd

# Carregar o conjunto de dados
data = pd.read_csv("data_0_KristenAndSara_1280x720_60_QP_37_Frames_0_features.csv", delimiter=';')

# Número de colunas
num_colunas = data.shape[1]
print("Número de colunas:", num_colunas)

# Verificar se há alguma linha com valores None em qualquer coluna
linhas_com_none = data[data.isna().any(axis=1)]
if not linhas_com_none.empty:
    print("Linhas com valores None:")
    print(linhas_com_none)
else:
    print("Não há linhas com valores None.")