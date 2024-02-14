import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#Carregar o conjunto os dados
data = pd.read_excel("StartUpsESG_0602.xlsx")
selected_columns = ['Country', 'Raised', 'ESG', 'E', 'S', 'G']
X = data[selected_columns].copy()  
X.fillna(0, inplace=True)  


if 'Country' in X.columns:
    # Normalizar os dados
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X[['Raised', 'ESG', 'E', 'S', 'G']])

    
    paises = X['Country'].unique()
    for pais in paises:
        X_pais = X[X['Country'] == pais]

        # Normalizar os dados específicos do país
        X_pais_scaled = scaler.fit_transform(X_pais[['Raised', 'ESG', 'E', 'S', 'G']])

        
        som = MiniSom(x=10, y=10, input_len=X_pais_scaled.shape[1], sigma=1.0, learning_rate=0.5)
        som.random_weights_init(X_pais_scaled)
        som.train_random(data=X_pais_scaled, num_iteration=100)

        # Escolher o vencedor
        bmu_idx = np.array([som.winner(x) for x in X_pais_scaled])

        
        clusters = np.array([np.ravel_multi_index(x, (10, 10)) for x in bmu_idx])

        X_pais['Cluster'] = clusters

        #Visualizar os clusters por país
        pca = PCA(n_components=2)
        X_pais_pca = pca.fit_transform(X_pais_scaled)
        plt.figure(figsize=(10, 6))
        plt.scatter(X_pais_pca[:, 0], X_pais_pca[:, 1], c=X_pais['Cluster'], cmap='Set1')
        plt.title(f'Clusters identificados pelo SOM para {pais} (PCA)')
        plt.xlabel('Componente Principal 1')
        plt.ylabel('Componente Principal 2')
        plt.colorbar(label='Cluster')
        plt.show()

        
        cluster_summary = X_pais.groupby('Cluster')['ESG'].describe()
        print(f"Estatísticas descritivas dos valores ESG por cluster para {pais}:")
        print(cluster_summary)
else:
    print("A coluna 'Country' não foi encontrada no conjunto de dados.")
