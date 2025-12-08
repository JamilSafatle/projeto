

import requests
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURAÇÃO ---
# COLA AQUI A TUA CHAVE DA GLASSNODE
GLASSNODE_API_KEY = "SUA_CHAVE_AQUI"
# --------------------

def coletar_on_chain():
    # Endpoint para 'Active Addresses' (Endereços Ativos)
    url = "https://api.glassnode.com/v1/metrics/addresses/active_count"

    # Parâmetros: 'a' é o ativo (BTC), 'i' é o intervalo (24h)
    parametros = {
        'a': 'BTC',
        'api_key': GLASSNODE_API_KEY,
        'i': '24h'
    }

    print("A conectar à API da Glassnode...")

    try:
        resposta = requests.get(url, params=parametros)

        if resposta.status_code == 200:
            dados = resposta.json()

            # A Glassnode retorna uma lista de dicionários: [{'t': timestamp, 'v': valor}, ...]
            lista_final = []

            for item in dados:
                timestamp = item['t']
                valor = item['v'] # Número de endereços ativos

                # Converter timestamp para data legível
                data = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

                lista_final.append([data, valor])

            # Criar DataFrame
            df = pd.DataFrame(lista_final, columns=['Data', 'Enderecos_Ativos'])

            # Salvar o arquivo
            caminho_arquivo = os.path.join('..', 'data', 'glassnode_enderecos_ativos.csv')

            # No Colab, se der erro de caminho, usa apenas: 'glassnode_enderecos_ativos.csv'
            # Mas mantemos a estrutura de pastas do projeto aqui:
            os.makedirs(os.path.join('..', 'data'), exist_ok=True)

            df.to_csv(caminho_arquivo, index=False)

            print(f"Sucesso! Dados salvos em: {caminho_arquivo}")
            print(f"Total de registos: {len(df)}")
            print("\n--- Amostra dos dados On-Chain ---")
            print(df.tail()) # Mostra os últimos dias para veres até onde a data vai

        else:
            print(f"Erro na Glassnode: {resposta.status_code}")
            print(resposta.text)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    coletar_on_chain()
