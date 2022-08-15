# churn_classifier
Ao fazer a análise exploratória foi percebida a existência de pequenas inconsistências que foram efetivamente ajustadas para melhorar a interpretação dos dados. A partir disso foi construído uma feature store com os principais atributos contidos na tabela.

O segundo step step consistiu em avaliar as variáveis que estavam dentro do dataset para verificar seu formato, critério, distribuição e a existência de dados faltantes. Comprovamos que algumas colunas não adicionavam informação, pelo que foram removidas. Seguidamente, foi feito um tratamento sobre os outliers, onde foi aplicada a regra dos 3 desvios para eliminá-los. 

Procedimentos de feature engineering foram feitos para discretizar alguns campos, além disso, fizemos o procedimento de One Hot Enconding e o balanceamento do dataset com a técnica de Under Sampling.

Os dados foram separados entre treino e teste, onde 80% dos dados foram selecionados para treinar o modelo. Assim, foi escolhido o XGBoost como modelo a ser utilizado para treinar e fazer as predições. Dentre os motivos para sua escolha encontram-se a rapidez do treino, a facilidade de usar em conjunto com outras libraries como sklearn, sua boa documentação. Em adição, este algoritmo permite definir uma métrica de avaliação a ser aprimorada após cada iteração; no caso foi escolhido o ROC.

A seleção dos hiperparâmetros foi feita em conjunto com GridCV, componente baseado em força bruta para escolher os melhores hipeparâmetros com base nas escolhas prévias.

Após o treino encontramos que as métricas reportadas em termos de F1-score, precision, recall, acurácia e AUC foram favoráveis, olhando para o precision e recall por grupo para achar o melhor threshold de separação entre as classes. Assim, decidiu-se que o melhor ponto de corte em 48.35%.

Finalizada a modelagem, encontramos o maior preditor utilizando feature importance, a variável ltv. Porém é importante citar a presença das varíaveis message e new friend.

Dentro das cinco principais preditoras, uma sobre a qual poderia se trabalhar é like. Essa variável, pode ser enriquecida por bases externas, interessante associar o engajamento do usuário, histórico, LTV  e dessa forma aumentar a possibilidade de cancelamento de forma inesperada. 

