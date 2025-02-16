import requests
import csv
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# URL da API do SIDRA para o IPCA
url = 'https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/63/p/all'

# Função para obter os dados do IPCA e salvar em CSV
def salvar_ipca_csv():
    # Obter o diretório de saída do arquivo .env
    output_dir = os.getenv('EXTRACT_OUTPUT_DIR')
    
    if not output_dir:
        print("Erro: Diretório de saída não definido no arquivo .env.")
        return

    # Verificar se o diretório existe; se não, criar
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Nome do arquivo CSV
    path_output_arquivo = os.path.join(output_dir, 'ipca.csv')

    # Fazer a requisição à API
    resposta = requests.get(url)

    if resposta.status_code == 200:
        data = resposta.json()

        # Filtrando os dados a partir de janeiro de 2020
        filtered_data = [entry for entry in data if entry["D3C"] >= "202001"]

        # Abrir o arquivo CSV para escrita
        with open(path_output_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            csv_file = csv.writer(arquivo)
            
            # Escrever o cabeçalho do CSV
            csv_file.writerow(['Mes (Codigo)', 'IPCA Variacao Mensal (%)'])
            
            # Escrever os dados no CSV
            for linha in filtered_data[1:]:  # Pular a primeira linha (cabeçalho da API)
                data = linha['D3C']
                valor = linha['V']
                csv_file.writerow([data, valor])
        
        print(f"Dados do IPCA salvos com sucesso em {path_output_arquivo}")
    else:
        print(f"Erro ao obter dados: {resposta.status_code}")

# Executar a função
salvar_ipca_csv()