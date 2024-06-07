# Esse programa tem como objetivo realizar uma análise de faturamento de uma determinada rede de lojas. Para isso, temos uma base de dados com informações de vendas e devoluções, e para automatizar esse processo, iremos seguir o seguinte passo a passo.


# Passo 1 - Percorrer todos os arquivos da paste base de dados (Pasta Vendas)
import os 

local_arquivos = os.listdir("/Users/kaiccesar/Documents/Estudos/Python/Hashtag/Vendas") 

# Passo 2 - Importar as bases de dados de vendas
for arquivo in local_arquivos: 

    if "vendas" in arquivo.lower():
        print(f"/Users/kaiccesar/Documents/Estudos/Python/Hashtag/Vendas/{arquivo}")
        # O "f" informa ao Python que esse texto aceita formatações dinâmicas 

# Passo 3 - Tratar / Compilar as bases de dados

# Passo 4 - Calcular o produto mais vendido (em quantidade)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - Criar um gráfico/dashboard
