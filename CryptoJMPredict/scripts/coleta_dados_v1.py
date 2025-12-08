

import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- TUA CHAVE AQUI ---
MINHA_API_KEY = "CG-MYQwAaABvHWzNDJE8tTCGSm4"
# ----------------------

def analisar_mercado_hoje():
    print("--- INICIANDO COLETA ATUALIZADA ---")

    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

    # Pedimos os últimos 365 dias
    parametros = {
        'vs_currency': 'usd',
        'days': '365',
        'interval': 'daily'
    }

    headers = {"accept": "application/json", "x-cg-demo-api-key": MINHA_API_KEY}

    print("1. Baixando dados...")
    resposta = requests.get(url, params=parametros, headers=headers)

    if resposta.status_code == 200:
        dados = resposta.json()

        # --- CORREÇÃO 1: Extrair a lista de volumes também ---
        precos = dados['prices']
        volumes = dados['total_volumes']

        lista_final = []

        # --- CORREÇÃO 2: Usar 'range' para pegar preço e volume ao mesmo tempo ---
        for i in range(len(precos)):
            timestamp = precos[i][0]
            preco = precos[i][1]

            # Tenta pegar o volume correspondente (proteção contra listas de tamanhos diferentes)
            if i < len(volumes):
                volume = volumes[i][1]
            else:
                volume = 0

            # Convertemos para data legível
            data = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')

            # Adicionamos os 3 itens: Data, Preço e Volume
            lista_final.append([data, preco, volume])

        # Agora sim, temos 3 colunas para 3 dados
        df = pd.DataFrame(lista_final, columns=['Data', 'Preco_Fechamento', 'Volume'])

        # --- FORMATAÇÃO ---
        df['Data'] = pd.to_datetime(df['Data'])
        df['Preco_Fechamento'] = df['Preco_Fechamento'].round(2)
        df['Volume'] = df['Volume'].astype(int) # Remove casas decimais do volume

        # Salvar com formatação para Excel em Português
        caminho_arquivo = 'bitcoin_historico.csv'
        df.to_csv(caminho_arquivo, index=False, sep=';', decimal=',')

        print(f"\nTotal de dias coletados: {len(df)}")

        print("\n--- PRIMEIROS 5 DIAS ---")
        print(df.head())

        print("\n--- ÚLTIMOS 5 DIAS (Deve incluir hoje/ontem) ---")
        print(df.tail())

        # --- VISUALIZAÇÃO GRÁFICA ---
        plt.figure(figsize=(12, 6))
        plt.plot(df['Data'], df['Preco_Fechamento'], label='Preço Bitcoin', color='#f7931a')
        plt.title('Histórico do Bitcoin: De 1 ano atrás até HOJE')
        plt.xlabel('Data')
        plt.ylabel('Preço (USD)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

        print(f"\nSucesso! Arquivo '{caminho_arquivo}' salvo corretamente.")

    else:
        print(f"Erro: {resposta.status_code}")
        print(resposta.text)

if __name__ == "__main__":
    analisar_mercado_hoje()


    
