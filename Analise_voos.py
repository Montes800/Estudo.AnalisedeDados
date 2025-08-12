# importando a biblioteca pandas
from google.colab import drive   # Importa o módulo para acessar arquivos do Google Drive no Colab
import pandas as pd              # Importa a biblioteca Pandas e dá o apelido 'pd' para facilitar o uso
import seaborn as sns             # Importa a biblioteca Seaborn para visualização de dados
import matplotlib.pyplot as plt   # Importa o módulo Pyplot do Matplotlib para criar gráficos

# Configuração de estilo
sns.set(style="whitegrid")        # Define o estilo visual dos gráficos do Seaborn (fundo branco com grades)

# Montar o Google Drive
drive.mount('/content/drive')     # Conecta o seu Google Drive ao Colab, criando o caminho /content/drive

# Caminho do arquivo
file_path = '/content/drive/MyDrive/airlines_flights_data.csv'
# Aqui você informa onde está o seu arquivo CSV dentro do Google Drive

# Ler o CSV
df = pd.read_csv(file_path)       # Lê o arquivo CSV e armazena os dados em um DataFrame Pandas chamado 'df'

# Visualizar as primeiras linhas
df.head()                         # Mostra as primeiras 5 linhas do DataFrame para inspecionar os dados

# Conta quantas ocorrências há para cada companhia aérea na coluna 'airline'
airline_counts = df['airline'].value_counts()

# Cria uma nova figura para o gráfico com tamanho 8x5 polegadas
plt.figure(figsize=(8,5))

# Cria um gráfico de barras com os nomes das companhias no eixo X
# e o número de voos (frequências) no eixo Y, usando a paleta de cores "viridis"
sns.barplot(x=airline_counts.index, y=airline_counts.values, palette="viridis")

# Define o título do gráfico
plt.title("Frequência das companhias aéreas")

# Define o nome do eixo Y
plt.ylabel("Número de voos")

# Define o nome do eixo X
plt.xlabel("Companhia Aérea")

# Rotaciona os rótulos do eixo X em 45 graus para evitar sobreposição
plt.xticks(rotation=45)

# Exibe o gráfico na tela
plt.show()

# Imprime a tabela de frequências no console para ver os valores exatos
print(airline_counts)

# Origem
plt.figure(figsize=(8,5)) # Cria uma figura com um tamanho de 8 polegadas de largura por 5 polegadas de altura
sns.countplot(
    data=df, # Define o DataFrame 'df' como a fonte de dados para o gráfico
    x='source_city', # Usa a coluna 'source_city' no eixo x, contando a frequência de cada cidade
    palette="coolwarm", # Aplica a paleta de cores 'coolwarm' nas barras
    order=df['source_city'].value_counts().index # Ordena as barras em ordem decrescente de frequência (da mais popular para a menos popular)
)
plt.title("Cidades de origem") # Adiciona o título "Cidades de origem" ao gráfico
plt.show() # Exibe o gráfico gerado

# Destino
plt.figure(figsize=(8,5)) # Cria uma figura com o mesmo tamanho para o segundo gráfico
sns.countplot(
    data=df, # Usa o mesmo DataFrame 'df'
    x='destination_city', # Usa a coluna 'destination_city' no eixo x
    palette="coolwarm", # Usa a mesma paleta de cores
    order=df['destination_city'].value_counts().index # Ordena as barras de destino por frequência
)
plt.title("Cidades de destino") # Adiciona o título "Cidades de destino" ao gráfico
plt.show() # Exibe o segundo gráfico

# Gráfico de Box Plot do Preço por Companhia Aérea
plt.figure(figsize=(10,6)) # Cria uma figura com dimensões de 10 polegadas de largura por 6 polegadas de altura
sns.boxplot(
    data=df, # Define o DataFrame 'df' como a fonte de dados
    x='airline', # A coluna 'airline' será usada no eixo x, representando as categorias (companhias aéreas)
    y='price', # A coluna 'price' será usada no eixo y, para analisar a distribuição de preços
    palette="husl" # Aplica a paleta de cores 'husl' aos box plots
)
plt.title("Preço por companhia aérea") # Adiciona um título ao gráfico
plt.xticks(rotation=45) # Gira os rótulos do eixo x em 45 graus para evitar sobreposição e facilitar a leitura
plt.show() # Exibe o gráfico na tela

# Partida
plt.figure(figsize=(10,6)) # Cria uma figura com 10 polegadas de largura e 6 de altura, ideal para visualização
sns.boxplot(
    data=df, # Usa o DataFrame 'df' como fonte de dados
    x='departure_time', # Define o eixo X com os horários de partida (manhã, tarde, noite)
    y='price', # Define o eixo Y com o preço, mostrando a distribuição para cada horário
    palette="Set3" # Aplica a paleta de cores 'Set3' para diferenciar os box plots
)
plt.title("Preço vs Horário de partida") # Adiciona um título descritivo ao gráfico
plt.show() # Exibe o primeiro gráfico


# Partida
plt.figure(figsize=(10,6)) # Cria uma figura com dimensões de 10x6 polegadas para o primeiro gráfico
sns.boxplot(
    data=df, # Define o DataFrame 'df' como a fonte de dados
    x='departure_time', # Plota os horários de partida no eixo x
    y='price', # Plota a distribuição de preços no eixo y
    palette="Set3" # Usa a paleta de cores 'Set3' para as caixas do gráfico
)
plt.title("Preço vs Horário de partida") # Adiciona um título ao gráfico
plt.show() # Exibe o gráfico

# Chegada
plt.figure(figsize=(10,6)) # Cria uma nova figura para o segundo gráfico
sns.boxplot(
    data=df, # Usa o mesmo DataFrame
    x='arrival_time', # Plota os horários de chegada no eixo x
    y='price', # Plota a distribuição de preços no eixo y
    palette="Set2" # Usa uma paleta de cores diferente, 'Set2', para este gráfico
)
plt.title("Preço vs Horário de chegada") # Adiciona um título ao segundo gráfico
plt.show() # Exibe o segundo gráfico

# Filtra o DataFrame para incluir apenas voos comprados com 1 ou 2 dias de antecedência
df_short_notice = df[df['days_left'].isin([1, 2])]

# Cria um gráfico de box plot
plt.figure(figsize=(10,6)) # Define o tamanho da figura (10 polegadas de largura, 6 de altura)
sns.boxplot(
    data=df_short_notice, # Usa o novo DataFrame filtrado como fonte de dados
    x='days_left', # Coloca o número de dias restantes (1 e 2) no eixo x
    y='price', # Coloca os preços no eixo y para analisar a distribuição
    palette="coolwarm" # Aplica a paleta de cores "coolwarm"
)
plt.title("Preço quando comprado 1 ou 2 dias antes") # Adiciona um título descritivo ao gráfico
plt.show() # Exibe o gráfico

# Gráfico de Box Plot para Preço por Classe
plt.figure(figsize=(8,5)) # Cria uma figura com um tamanho de 8x5 polegadas
sns.boxplot(
    data=df, # Utiliza o DataFrame 'df' como a fonte de dados
    x='class', # Coloca as categorias de classe (ex: Economy, Business) no eixo x
    y='price', # Coloca os valores de preço no eixo y para mostrar a distribuição
    palette="pastel" # Aplica a paleta de cores "pastel" para os box plots
)
plt.title("Preço por classe") # Adiciona o título "Preço por classe" ao gráfico
plt.show() # Exibe o gráfico na tela

# Define as condições de filtragem
filtro = (df['airline'] == 'Vistara') & \
         (df['source_city'] == 'Delhi') & \
         (df['destination_city'] == 'Hyderabad') & \
         (df['class'] == 'Business')

# Aplica o filtro no DataFrame e calcula a média da coluna 'price'
preco_medio = df[filtro]['price'].mean()

# Imprime o resultado formatado, mostrando o preço médio com duas casas decimais
print(f"Preço médio: ₹{preco_medio:.2f}")