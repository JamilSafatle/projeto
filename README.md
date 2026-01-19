# 📈 Bitcoin Predictor LSTM

Este projeto é um sistema end-to-end de previsão de preços de Bitcoin utilizando Deep Learning (Redes Neurais LSTM). O sistema coleta dados financeiros e de sentimento (notícias), processa indicadores técnicos e executa previsões diárias automaticamente via GitHub Actions.

## 🚀 Funcionalidades
- **Coleta Automática:** Integração com APIs da CoinGecko e Google News.
- **Análise de Sentimento:** Processamento de linguagem natural (VADER) em manchetes de notícias.
- **Engenharia de Features:** Cálculo automático de RSI, SMA-7 e SMA-21.
- **Deep Learning:** Modelo LSTM (Long Short-Term Memory) treinado com histórico de preços.
- **CI/CD Pipeline:** Automação via GitHub Actions para inferência diária sem intervenção humana.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10
- **IA/ML:** TensorFlow/Keras, Scikit-learn
- **Dados:** Pandas, NumPy
- **Automação:** GitHub Actions (YAML)

## 📊 Performance do Modelo
- **Arquitetura:** LSTM (128 units) -> Dropout -> LSTM (64 units) -> Dense
- **Erro Médio Absoluto (MAE):** ~$2,490 USD (aprox. 2.5% de erro no teste cego)
- **Janela de Tempo:** O modelo analisa os últimos 60 dias para prever o próximo.

## 🤖 Automação (Previsão Diária)
O sistema roda automaticamente todos os dias às 09:00 UTC.
Para ver a previsão de hoje, vá até a aba **Actions** > **Previsão Diária Bitcoin** > Clique na última execução > **Executar IA de Previsão**.

---
