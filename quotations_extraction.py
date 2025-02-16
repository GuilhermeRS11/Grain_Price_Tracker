import requests
import json

# Base URL of the API
BASE_URL = "http://painel.cotrisel.com/api/v1/quotations"

# Function to fetch data from a page
def fetch_page_data(page, retries=3):
    url = f"{BASE_URL}?page={page}"
    for _ in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error accessing page {page}: {e}")
    return None

# Function to save data to a JSON file
def save_to_json(data, file_name="quotations_prices.json"):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data saved in '{file_name}'")

# Main function to extract all data
def extract_all_data():
    all_data = []
    page = 1
    
    while True:
        print(f"Fetching data from page {page}...")
        json_data = fetch_page_data(page)
        
        if not json_data or not json_data["data"]["items"]["data"]:
            break
        
        # Add the items from the current page to the complete list
        all_data.extend(json_data["data"]["items"]["data"])
        
        # Check if there is a next page
        if json_data["data"]["items"]["next_page_url"] is None:
            break
        
        page += 1
    
    return all_data

# Execute the extraction and save to JSON
if __name__ == "__main__":
    data = extract_all_data()
    if data:
        save_to_json(data)
