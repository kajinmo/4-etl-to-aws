# ETL

## Extract
Passo 1: Entender a API do SIDRA
O SIDRA (Sistema IBGE de Recuperação Automática) disponibiliza tabelas de dados. Para o IPCA, a tabela relevante é a Tabela 1737, que contém os índices mensais do IPCA.

A URL base da API é:

```
https://apisidra.ibge.gov.br/values/t/{tabela}/{n1}/{n2}/{n3}/{n4}/{n5}/{n6}/{n7}/{n8}/{n9}
```
Onde:

{tabela} é o código da tabela (no caso, 1737).

{n1} a {n9} são parâmetros opcionais para filtrar os dados (por exemplo, período, variáveis, etc.).