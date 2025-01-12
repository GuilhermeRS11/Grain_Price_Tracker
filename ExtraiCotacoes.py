import requests
import json

# URL base da API
BASE_URL = "http://painel.cotrisel.com/api/v1/quotations"

# Função para obter dados de uma página
def fetch_page_data(page):
    url = f"{BASE_URL}?page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar a página {page}: {response.status_code}")
        return None

# Função para salvar os dados em um arquivo JSON
def save_to_json(data, file_name="cotacoes.json"):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Dados salvos em '{file_name}'")

# Função principal para extrair todos os dados
def extract_all_data():
    all_data = []
    page = 1
    
    while True:
        print(f"Buscando dados da página {page}...")
        json_data = fetch_page_data(page)
        
        if not json_data or not json_data["data"]["items"]["data"]:
            break
        
        # Adiciona os itens da página atual à lista completa
        all_data.extend(json_data["data"]["items"]["data"])
        
        # Verifica se há uma próxima página
        if json_data["data"]["items"]["next_page_url"] is None:
            break
        
        page += 1
    
    return all_data

# Executa a extração e salva em JSON
if __name__ == "__main__":
    data = extract_all_data()
    if data:
        save_to_json(data)
