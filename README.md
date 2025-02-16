# 📊 Grain Price Analysis - São Sepé/RS

This project collects and analyzes the prices of different grains (rice, corn, soy, sorghum, and wheat) published by **Cotrisel**, a company located in São Sepé, Rio Grande do Sul, Brazil. The goal is to provide a clear visualization of price trends over time.

## 🚀 Features

✅ **Data extraction:** Retrieves grain prices directly from Cotrisel's API.  
✅ **Storage:** Saves the collected data in a JSON file for further analysis.  
✅ **Trend visualization:** Generates graphs to better understand price variations.

---

## 🛠️ Installation and Dependencies

Before running the project, you need to install the required Python packages.  
You can install them using **pip**:

```bash
pip install requests matplotlib
```

## 📌 How to Use

The project is divided into two main steps: **data collection** and **price analysis**.

### **1️⃣ Data Collection**
The `quotations_extraction.py` script accesses the Cotrisel API, extracts the available grain prices, and stores the data in a JSON file for further analysis.

To run the data collection process, use the following command:

```bash
python quotations_extraction.py
```

This will create a file named `quotations_prices.json`, containing the collected data.

### **2️⃣ Price Analysis**
The `quotations_analyses.py` script processes the extracted data, corrects inconsistent values, and generates graphs illustrating the variation of grain prices over time.

To visualize the graphs, execute:

```bash
python quotations_analyses.py
```

If the data was successfully collected, the script will display graphs representing the price trends.

📊 **Graph 1 - Grain Price Trends**  

![Graph 1](/images/quotations.png)
