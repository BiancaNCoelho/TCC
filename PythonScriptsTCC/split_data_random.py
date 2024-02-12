import pandas as pd

# Carrega o dataset
df = pd.read_csv("output.csv")

# Define a proporção para o split (por exemplo, 80% para treino e 20% para teste)
test_size = 0.3

# Faz o split
train_df = df.sample(frac=1-test_size, random_state=42)
test_df = df.sample(frac=test_size, random_state=42)

#Criar um novo DataFrame com as linhas removidas
dataset_removido = test_df.copy()

# Remover as linhas do dataset original
df.drop(test_df.index, inplace=True)

# Salvar o dataset original sem as linhas removidas
df.to_csv('output.csv', index=False)

# Salvar o dataset com as linhas removidas
dataset_removido.to_csv('dataset_linhas_removidas.csv', index=False)
