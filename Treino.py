from os import listdir
from os import chdir
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from collections import Counter
from imblearn.under_sampling import RandomUnderSampler
import m2cgen as m2c
import gc


#---------------------------------------------------------------------------------------------------------------------
#função para aplicar o modelo da DT
def apply_Decision_Tree(_X_train, _y_train, _nome_arq, _save_path):

	model_decison_tree_class = DecisionTreeClassifier(random_state = 42, max_depth = 7)

	#realiza o treinamento do modelo
	model_decison_tree_class.fit(_X_train,_y_train)

	code_DT_em_C = m2c.export_to_c(model_decison_tree_class)

	file = open(_save_path+'DT_w_'+_nome_arq+'.cpp', 'w') 
	file.write(code_DT_em_C)
	file.close() 
#---------------------------------------------------------------------------------------------------------------------



#caminho onde se encontram os arquivos com as features
load_path_treino = "/home/rgsviana/Fernando/machine/modelo_por_tam_bloco/128x128/_all_treino_128x128.csv"
save_path =        "/home/rgsviana/Fernando/machine/modelo_por_tam_bloco/128x128/"
#load_path_teste =  
#save_path_teste =  

#lista com as features que serão utilizadas na machine
# -- Bianca --
# feautures utilizadas abaixo são para Unidirecional e Bidirecional
features = [
    'tamBlocoWidth',
    'tamBlocoHeight',
    'numQp',
    'POC',
    'widthVideo',
    'heightVideo',
    'cu_pos_X',
    'cu_pos_Y',
    'imv',
    'atual_QP',
    'mv_uni_L0_Hor_X',
    'mv_uni_L0_Ver_Y',
    'mv_uni_L1_Hor_X',
    'mv_uni_L1_Ver_Y',
    'mv_Pred_Uni_L0_Hor_X',
      'mv_Pred_Uni_L0_Ver_Y',
      'mv_Pred_Uni_L1_Hor_X',
      'mv_Pred_Uni_L1_Ver_Y',
      'cost_Mv_Uni_L0',
      'cost_Mv_Uni_L1',
      'bits_Mv_Uni_L0',
      'bits_Mv_Uni_L1',
      'bidirecional_pai',
      'custo_pai',
      'imv_pai',
      'bidirecional_vizEsq',
      'custo_vizEsq',
      'imv_vizEsq',
      'bidirecional_acima',
      'custo_acima',
      'imv_acima',
      'sum',
      'media',
      'vari',
      'gradH',
      'gradV',
      'razao_grad',
      'grad_razao_pixels',
      'desvioPadrao',
      'dist_uni_L0_L1',
      'bloco_atual_bidirecional'
		]

df_treino = pd.read_csv(load_path_treino, delimiter = ';')
y_treino = df_treino.cu_atual_affine
X_treino = df_treino[features]

df_teste = pd.read_csv(load_path_teste, delimiter = ';')
y_teste = df_teste.cu_atual_affine
X_teste = df_teste[features]

print("RAMIRO")
print("Antes")
print(Counter(y_treino))

undersample = RandomUnderSampler(sampling_strategy = 'majority', random_state = 12)

X_under, y_under = undersample.fit_resample(X_treino, y_treino)
X_t, y_t = undersample.fit_resample(X_teste, y_teste)

print("Depois Under")
print(Counter(y_under))
print(Counter(y_t))

model_decison_tree_class = DecisionTreeClassifier(random_state = 42, max_depth = 10)
model_decison_tree_class.fit(X_under, y_under)
val_predictions = model_decison_tree_class.predict(X_t)
print("Precision")
print(precision_score(y_t, val_predictions))
print("Recall")
print(recall_score(y_t, val_predictions))
print("F1")
print(f1_score(y_t, val_predictions))

apply_Decision_Tree(X_under, y_under, "TodosTamanhos", save_path)
