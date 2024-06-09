# Esse programa tem como objetivo realizar uma análise básica de faturamento de uma determinada rede de lojas. Para isso, temos uma base de dados com informações de vendas e devoluções, e para automatizar esse processo, iremos seguir o seguinte passo a passo.


# Passo 1 - Percorrer todos os arquivos da paste base de dados (Pasta Vendas)
import os
import pandas as pd # as pd (apelido) 
 
local_arquivos = os.listdir("/Users/kaiccesar/Documents/Estudos/Python/Hashtag/Vendas") 
tabela_total = pd.DataFrame()


# Passo 2 - Importar as bases de dados de vendas
for arquivo in local_arquivos: 

    if "vendas" in arquivo.lower():
        # Importar arquivo
        tabela = pd.read_csv(f"/Users/kaiccesar/Documents/Estudos/Python/Hashtag/Vendas/{arquivo}")
        # O "f" informa ao Python que esse texto aceita formatações dinâmicas 

# Passo 3 - Tratar / Compilar as bases de dados
        tabela_total = tabela_total._append(tabela) # Adiciona as tabelas para uma única tabela


# Passo 4 - Calcular o produto mais vendido (em quantidade)

tabela_produtos = tabela_total.groupby('Produto').sum()
# Agrupa a coluna que passamos como referência e soma todas as outras colunas
# OBS: Quando é usado o groupby, a referência que foi passada, agora se torna um índice. Na criação da dashboard, deve se atentar quando passar os eixos 

tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)


# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
# Criando uma nova coluna dentro da tabela, passando duas colunas e sua operação aritmética

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)


# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) 
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

# Passo 7 - Criar um Gráfico/Dashboard

import plotly.express as px

grafico = px.area(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()