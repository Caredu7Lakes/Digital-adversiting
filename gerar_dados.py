import pandas as pd
import numpy as np

# Criando os dados simulados que conversamos
np.random.seed(42)
n_pacientes = 100

data = {
    'ID': range(1, n_pacientes + 1),
    'Akkermansia_muciniphila': np.random.uniform(0, 5, n_pacientes),
    'Proteobacteria': np.random.uniform(1, 15, n_pacientes),
    'BCAAs_Totais': np.random.normal(500, 100, n_pacientes),
    'Butirato_Fecal': np.random.uniform(10, 60, n_pacientes),
    '3_Methylhistidine': np.random.normal(50, 10, n_pacientes),
    'IMC': np.random.uniform(28, 45, n_pacientes),
    'HbA1c': np.random.uniform(5.5, 8.5, n_pacientes)
}

df = pd.DataFrame(data)

# SALVANDO O ARQUIVO NA SUA PASTA
df.to_csv('base_dados_omica_tirzepatida.csv', index=False)
print("Arquivo 'base_dados_omica_tirzepatida.csv' criado com sucesso na sua pasta!")
