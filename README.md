# Análise de Dados de Voos e Companhias Aéreas ✈️

## Descrição do Projeto 📊

Este projeto é uma análise exploratória de dados de voos, com o objetivo de extrair insights sobre o mercado de passagens aéreas. Utilizando um conjunto de dados que contém informações detalhadas sobre voos, companhias aéreas, cidades de origem e destino, horários e preços, o projeto responde a uma série de perguntas-chave sobre a precificação e a logística dos voos.

As análises foram realizadas em Python, utilizando as bibliotecas `Pandas` para manipulação dos dados e `Matplotlib` e `Seaborn` para visualização.

## Fonte dos Dados 📁

O conjunto de dados utilizado neste projeto foi obtido na plataforma Kaggle, disponível no seguinte link:
[Airlines Flights Data - Rohit Grewal](https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data/data)

## Perguntas de Análise ❓

A seguir, estão as perguntas que foram respondidas através da análise dos dados:

1.  Quais são as companhias aéreas com maior número de voos no conjunto de dados?
2.  Quais são as cidades de origem e destino mais movimentadas?
3.  O preço das passagens varia de acordo com a companhia aérea?
4.  O horário de partida e de chegada impacta o preço das passagens?
5.  Como o preço das passagens muda com a alteração da origem e do destino?
6.  O preço é afetado quando as passagens são compradas de última hora (1 ou 2 dias antes)?
7.  Qual a diferença de preço entre as classes Econômica e Executiva?
8.  Qual é o preço médio de um voo específico (ex: Vistara, de Delhi para Hyderabad, na Classe Executiva)?

## Tecnologias Utilizadas 🛠️

* **Python:** 🐍 Linguagem de programação principal.
* **Pandas:** 🐼 Para manipulação e análise de dados.
* **Matplotlib:** 📈 Para criação de gráficos e visualizações.
* **Seaborn:** 🎨 Para criação de gráficos estatísticos mais avançados.

## Estrutura do Repositório 📂

* `airlines_flights_data.csv`: O conjunto de dados original utilizado na análise.
* `analise_voos.py`: O script Python contendo todo o código para a análise e a geração dos gráficos.

## Como Executar o Código 💻

Para executar a análise, você precisará ter Python e as bibliotecas listadas instaladas.
1.  Clone este repositório para sua máquina local.
2.  Certifique-se de que o arquivo `airlines_flights_data.csv` está na mesma pasta que o script `analise_voos.py`.
3.  Abra um terminal e execute o script:
    ```bash
    python analise_voos.py
    ```
Os gráficos serão exibidos em janelas separadas.
