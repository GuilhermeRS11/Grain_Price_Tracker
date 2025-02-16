# 📊 Análise de Cotações de Grãos - São Sepé/RS

Este projeto coleta e analisa os preços de diferentes grãos (arroz, milho, soja, sorgo e trigo) publicados pela **Cotrisel**, uma firma localizada em São Sepé, Rio Grande do Sul. O objetivo é fornecer uma visualização clara das tendências de preços ao longo do tempo.

## 🚀 Funcionalidades

✅ **Extração de dados:** Obtém os preços diretamente da API da Cotrisel.  
✅ **Armazenamento:** Salva os dados coletados em um arquivo JSON para posterior análise.  
✅ **Visualização de tendências:** Gera gráficos para melhor entendimento das variações de preços.

---

## 🛠️ Instalação e Dependências

Antes de executar o projeto, é necessário instalar os pacotes Python necessários.  
Você pode instalá-los utilizando o **pip**:

```bash
pip install requests matplotlib
```

## 📌 Como Usar

O projeto é dividido em duas etapas: **coleta dos dados** e **análise das cotações**.

### **1️⃣ Coleta dos Dados**
O script `quotations_extraction.py` acessa a API da Cotrisel, extrai as cotações de grãos disponíveis e armazena os dados em um arquivo JSON para análise posterior.

Para executar a coleta de dados, utilize o seguinte comando:

```bash
python quotations_extraction.py
```

Isso criará um arquivo chamado `quotations_prices.json`, contendo os dados coletados.

### **2️⃣ Análise das Cotações**
O script `quotations_analyses.py` processa os dados extraídos, corrige valores inconsistentes e gera gráficos que ilustram a variação dos preços dos grãos ao longo do tempo.

Para visualizar os gráficos, execute:

```bash
python quotations_analyses.py
```

Se os dados foram coletados corretamente, o script exibirá gráficos representando a evolução dos preços.

📊 **Gráfico 1 - Evolução dos preços dos grãos**  

![Gráfico 1](/images/quotations.png)

