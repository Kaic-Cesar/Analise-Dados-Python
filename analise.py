# Esse programa tem como objetivo realizar uma análise de faturamento de uma determinada rede de lojas. Para isso, temos uma base de dados com informações de vendas e devoluções, e para automatizar esse processo, iremos seguir o seguinte passo a passo.


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

print(tabela_total)
# Passo 4 - Calcular o produto mais vendido (em quantidade)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - Criar um Gráfico/Dashboard
