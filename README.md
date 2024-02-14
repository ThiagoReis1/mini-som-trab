# mini-som-trab


No contexto deste trabalho de análise de dados das startups, foram explorados dois algoritmos de clustering: o KMeans e o MiniSom. Ambos foram empregados com o objetivo de identificar padrões nos dados e agrupar as startups com base em diferentes critérios, como país de origem, montante levantado e valores ESG (Environmental, Social, and Governance). A aplicação desses algoritmos possibilitou uma segmentação das startups em clusters distintos, o que é fundamental para compreender melhor a distribuição e as características dessas empresas em um espaço multidimensional.


Uma das principais diferenças entre o KMeans e o MiniSom reside na abordagem de clustering. Enquanto o KMeans é um algoritmo de particionamento que divide os dados em K clusters definidos, minimizando a variância intra-cluster, o MiniSom é uma técnica baseada em redes neurais auto-organizáveis que organiza os neurônios em uma grade topológica para representar os clusters. Essa diferenciação na estratégia de clustering pode influenciar a forma como os clusters são formados e como são interpretados.


Além disso, a visualização dos clusters também difere entre os algoritmos. O MiniSom oferece uma representação visual direta dos clusters em uma grade bidimensional, o que facilita a interpretação dos resultados. Por outro lado, o KMeans requer técnicas adicionais, como redução de dimensionalidade, para visualizar os clusters em um espaço de menor dimensão, como o PCA (Principal Component Analysis).


A interpretação dos resultados gerados pelos algoritmos também varia. Enquanto o KMeans fornece uma atribuição direta de cada ponto de dados a um cluster específico, o MiniSom pode exigir uma análise mais aprofundada devido à organização topológica dos neurônios na grade. Isso pode resultar em uma compreensão mais complexa dos clusters e das relações entre os dados.


Em suma, a escolha entre o KMeans e o MiniSom depende das características dos dados e dos objetivos da análise. Ambos os algoritmos oferecem vantagens e desvantagens, e a comparação entre os resultados obtidos com cada um pode fornecer insights valiosos sobre as startups e suas relações com os critérios de clusterização considerados.
