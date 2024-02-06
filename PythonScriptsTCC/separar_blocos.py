# Separar em blocos
# tamBlocoWidth - tamBlocoHeight
# 4x8 e 8x4 are out
#

import csv
import os
import pandas as pd

def separate_csv_by_dimensions(input_file, output_folder):
    df = pd.read_csv(input_file, delimiter=';')

    # Crie um diretório de saída se não existir
    os.makedirs(output_folder, exist_ok=True)
    
    #print("Colunas:", df.columns)

    # GroupBy nas colunas 'Width' e 'Height' e itere sobre os grupos
    grouped = df.groupby(['tamBlocoWidth', 'tamBlocoHeight'])
    for (width, height), group in grouped:
        dimensions_str = f"{width}x{height}"
        output_file = os.path.join(output_folder, f"output_{dimensions_str}.csv")

        print(f"Creating file: {output_file}")

        group.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_csv = "KristenAndSara_1280x720_60_QP_37_Frames_0_features.csv"
  
    output_directory = "pasta_de_saida"

    separate_csv_by_dimensions(input_csv, output_directory)
