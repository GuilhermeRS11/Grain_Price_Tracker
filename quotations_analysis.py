import json
import matplotlib.pyplot as plt
from datetime import datetime

# Function to load data from JSON file
def load_data(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# Function to process the data
def process_data(data):
    dates = []
    rice_prices = []
    corn_prices = []
    soy_prices = []
    sorghum_prices = []
    wheat_prices = []

    for item in data:
        # Convert the date to datetime format
        date = datetime.strptime(item["created_date"], "%d/%m/%Y")
        dates.append(date)
        
        # If the value is zero(and it's not the first element), it is an outlier and should not be considered, assign the previous value
        if item["rice"] == "0.00" and data.index(item) != 0:
            item["rice"] = data[data.index(item) - 1]["rice"]
        if item["corn"] == "0.00"and data.index(item) != 0:
            item["corn"] = data[data.index(item) - 1]["corn"]
        if item["soy"] == "0.00"and data.index(item) != 0:
            item["soy"] = data[data.index(item) - 1]["soy"]
        if item["sorghum"] == "0.00"and data.index(item) != 0:
            item["sorghum"] = data[data.index(item) - 1]["sorghum"]
        if item["wheat"] == "0.00"and data.index(item) != 0:
            item["wheat"] = data[data.index(item) - 1]["wheat"]
  
        rice_prices.append(float(item["rice"]))
        corn_prices.append(float(item["corn"]))
        soy_prices.append(float(item["soy"]))
        sorghum_prices.append(float(item["sorghum"]))
        wheat_prices.append(float(item["wheat"]))

    return dates, rice_prices, corn_prices, soy_prices, sorghum_prices, wheat_prices

# Function to plot the graphs
def plot_data(dates, rice, corn, soy, sorghum, wheat):
    # General Chart
    plt.figure(figsize=(10, 6))
    plt.plot(dates, rice, label="Rice", marker="o")
    plt.plot(dates, corn, label="Corn", marker="o")
    plt.plot(dates, soy, label="Soy", marker="o")
    plt.plot(dates, sorghum, label="Sorghum", marker="o")
    plt.plot(dates, wheat, label="Wheat", marker="o")
    plt.xlabel("Date")
    plt.ylabel("Price (R$)")
    plt.title("Prices Over Time")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Soybean Chart
    plt.figure(figsize=(10, 6))
    plt.plot(dates, soy, label="Soy", color="green", marker="o")            
    plt.xlabel("Date")
    plt.ylabel("Price (R$)")
    plt.title("Soybean Price Over Time")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Name of the JSON file generated in the previous code
json_file = "quotations_prices.json"

# Execute the flow
try:
    # Load and process the data
    data = load_data(json_file)
    dates, rice_prices, corn_prices, soy_prices, sorghum_prices, wheat_prices = process_data(data)

    # Plot the graphs
    plot_data(dates, rice_prices, corn_prices, soy_prices, sorghum_prices, wheat_prices)
except FileNotFoundError:
    print(f"File '{json_file}' not found. Make sure the file exists in the directory.")
except Exception as e:
    print(f"An error occurred: {e}")
