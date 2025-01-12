import json
import matplotlib.pyplot as plt
from datetime import datetime

# Função para carregar os dados do arquivo JSON
def load_data(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# Função para processar os dados
def process_data(data):
    dates = []
    rice_prices = []
    corn_prices = []
    soy_prices = []
    sorghum_prices = []
    wheat_prices = []

    for item in data:
        # Converte a data para o formato datetime
        date = datetime.strptime(item["created_date"], "%d/%m/%Y")
        dates.append(date)
        
        # Se o valor for zero, é um outlier e não deve ser considerado e atribui o valor anteior
        if item["rice"] == "0.00":
            item["rice"] = data[data.index(item) - 1]["rice"]
        if item["corn"] == "0.00":
            item["corn"] = data[data.index(item) - 1]["corn"]
        if item["soy"] == "0.00":
            item["soy"] = data[data.index(item) - 1]["soy"]
        if item["sorghum"] == "0.00":
            item["sorghum"] = data[data.index(item) - 1]["sorghum"]
        if item["wheat"] == "0.00":
            item["wheat"] = data[data.index(item) - 1]["wheat"]
  
        rice_prices.append(float(item["rice"]))
        corn_prices.append(float(item["corn"]))
        soy_prices.append(float(item["soy"]))
        sorghum_prices.append(float(item["sorghum"]))
        wheat_prices.append(float(item["wheat"]))

    return dates, rice_prices, corn_prices, soy_prices, sorghum_prices, wheat_prices

# Função para plotar os gráficos
def plot_data(dates, rice, corn, soy, sorghum, wheat):
    # Gráfico Geral
    plt.figure(figsize=(10, 6))
    plt.plot(dates, rice, label="Arroz", marker="o")
    plt.plot(dates, corn, label="Milho", marker="o")
    plt.plot(dates, soy, label="Soja", marker="o")
    plt.plot(dates, sorghum, label="Sorgo", marker="o")
    plt.plot(dates, wheat, label="Trigo", marker="o")
    plt.xlabel("Data")
    plt.ylabel("Cotação (R$)")
    plt.title("Cotações ao Longo do Tempo")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Gráfico da Soja
    plt.figure(figsize=(10, 6))
    plt.plot(dates, soy, label="Soja", color="green", marker="o")

    # Adiciona linhas verticais para todos os meses de maio (apenas para o 1 dia de maio)
    for date in dates:
        if date.month == 5:  # Verifica se o mês é maio
            plt.axvline(date, color="red", linestyle="--", alpha=0.3)
            
    plt.xlabel("Data")
    plt.ylabel("Cotação (R$)")
    plt.title("Cotação da Soja ao Longo do Tempo")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# Nome do arquivo JSON gerado no código anterior
json_file = "cotacoes.json"

# Executa o fluxo
try:
    # Carrega e processa os dados
    data = load_data(json_file)
    dates, rice_prices, corn_prices, soy_prices, sorghum_prices, wheat_prices = process_data(data)

    # Plota os gráficos
    plot_data(dates, rice_prices, corn_prices, soy_prices, sorghum_prices, wheat_prices)
except FileNotFoundError:
    print(f"Arquivo '{json_file}' não encontrado. Certifique-se de que o arquivo existe no diretório.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
