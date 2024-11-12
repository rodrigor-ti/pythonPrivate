# -*- coding: utf-8 -*-
"""Atividade05.2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LeoM94RRJ4Ykdqzbqw3V26jXF6es0Itv
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd

df = pd.read_csv('advertising.csv')
desc_stats = df.describe()
print("\nEstatísticas Descritivas:")
print(desc_stats)

"""**`Naive Bayes Gaussiano`**"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X = dados[['tempo_diario_site', 'idade', 'renda_media_regiao', 'tempo_medio_internet', 'sexo']]
y = dados['clique']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))

"""**Random Forest**"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Pré-processar os dados
df = dados.select_dtypes(include=['float64', 'int64']).copy()
df = dados.fillna(df.mean())

# Identificar colunas com valores de string
colunas_categoricas = df.select_dtypes(include=['object']).columns

# Aplicar Label Encoding para converter strings em números
label_encoder = LabelEncoder()
for coluna in colunas_categoricas:
    df[coluna] = label_encoder.fit_transform(df[coluna])

# Dividir os dados em conjuntos de treinamento e teste
X = df.drop('clique', axis=1)
y = df['clique']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de floresta aleatória
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões e avaliar o modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

"""**K-Nearest Neighbors (KNN):**"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Pré-processar os dados
df = dados.select_dtypes(include=['float64', 'int64']).copy()
df = dados.fillna(df.mean())

# Identificar colunas com valores de string
colunas_categoricas = df.select_dtypes(include=['object']).columns

# Aplicar Label Encoding para converter strings em números
label_encoder = LabelEncoder()
for coluna in colunas_categoricas:
    df[coluna] = label_encoder.fit_transform(df[coluna])

# Dividir os dados em conjuntos de treinamento e teste
X = df.drop('clique', axis=1)
y = df['clique']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)  # Now the data should be all numeric

# Fazer previsões e avaliar o modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

"""**b) Implemente pelo menos três algoritmos preditivos para classificação. Explique se os resultados foram bons. Qual algoritmo foi melhor?**

Os resultados dos modelos Naive Bayes Gaussiano e Random Forest foram muito bons, com uma precisão de 0.945 e 0.94, respectivamente. Isso significa que esses modelos foram capazes de prever corretamente se um usuário clicaria ou não em cerca de 94-95% dos casos, o que é um desempenho muito bom.
No entanto, o desempenho do modelo K-Nearest Neighbors (KNN) foi significativamente menor, com uma precisão de apenas 0.61. Isso significa que o modelo KNN foi capaz de prever corretamente apenas em cerca de 61% dos casos.

**Melhor algoritimo:** Dentre os 3 utilizados (Naive Bayes Gaussiano, Random Forest e KNN) o que teve melhor resultado foi o Naive Bayes Gaussiano com a precisão de 0.945.
"""