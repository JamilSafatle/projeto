import pandas as pd
import matplotlib.pyplot as plt
import os

def visualizar_dados():
    # 1. Carregar o arquivo CSV
    # CORREÇÃO AQUI: Mudamos o nome para bater com o que está na tua barra lateral
    caminho_arquivo = 'bitcoin_historico.csv'

    try:
        print(f"Lendo o arquivo: {caminho_arquivo}...")

        # Leitura formatada para Excel em Português (ponto e vírgula e vírgula decimal)
        df = pd.read_csv(caminho_arquivo, sep=';', decimal=',')

        # 2. Converter a coluna 'Data' para o formato datetime
        df['Data'] = pd.to_datetime(df['Data'])

        # Configurar a Data como índice
        df.set_index('Data', inplace=True)

        print("Primeiras 5 linhas dos dados carregados:")
        print(df.head())

        # 3. Plotar o gráfico
        print("\nGerando gráfico...")
        plt.figure(figsize=(12, 6))

        # Plotamos o Preço
        plt.plot(df.index, df['Preco_Fechamento'], label='Preço Bitcoin (USD)', color='#f7931a', linewidth=2)

        plt.title('Análise Exploratória: Histórico de Preço do Bitcoin')
        plt.xlabel('Data')
        plt.ylabel('Preço (USD)')
        plt.legend()
        plt.grid(True, alpha=0.3)

        # Mostrar o gráfico
        plt.show()

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Verifique se o nome do arquivo na barra lateral esquerda é EXATAMENTE igual ao do código.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    visualizar_dados()
