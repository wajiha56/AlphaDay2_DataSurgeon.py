# 🩺 AlphaDay2: Data Surgeon – Python Data Cleaning Project

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Pandas](https://img.shields.io/badge/Pandas-2.1.0-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Project Overview
This project demonstrates **professional data cleaning and preprocessing skills** using Python, applied to a messy sales dataset.  
The dataset contains missing values, typos, and extreme outliers, simulating a real-world scenario where raw data must be corrected before analysis or AI workflows.

**Skills Demonstrated:**
- Data Imputation (handling missing values carefully)  
- Outlier Detection and Correction  
- Data Validation & Verification  
- Professional workflow execution for remote data science roles  

---

## 📊 Dataset
- **File:** `broken_sales_data.csv`  
- **Columns:** `Order_ID`, `Date`, `Region`, `Category`, `Product`, `Sales`, `Quantity`, `Profit`  
- **Data Issues:**  
  - Missing `Sales` for some Electronics products  
  - Missing `Quantity` for Furniture items  
  - Outlier quantity values (e.g., 5,000 units for Paper)  
  - Negative profit values  

**Sample Data:**

| Order_ID | Date       | Region | Category    | Product   | Sales   | Quantity | Profit |
|----------|------------|--------|------------|-----------|--------|---------|--------|
| 111      | 2026-01-10 | North  | Electronics | Smartphone | NaN    | 1       | 5000   |
| 112      | 2026-01-15 | West   | Office      | Paper      | 1200   | 5000    | 300    |
| 113      | 2026-01-20 | East   | Furniture   | Chair      | 8500   | NaN     | 600    |

---

## 🛠 Technical Workflow

### 1. Load & Inspect Data
```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/broken_sales_data.csv')

# Check for missing values
print(df.isnull().sum())
# Fill missing Sales for Electronics with category median
median_sales = df[df['Category']=='Electronics']['Sales'].median()
df.loc[(df['Category']=='Electronics') & (df['Sales'].isnull()), 'Sales'] = median_sales

# Fill missing Quantity for Chair with 1
df.loc[(df['Product']=='Chair') & (df['Quantity'].isnull()), 'Quantity'] = 1

# Any Quantity > 100 → replace with Office category mean
office_mean = df[df['Category']=='Office']['Quantity'].mean()
df.loc[df['Quantity'] > 100, 'Quantity'] = office_mean

# Verify data
print(df.isnull().sum())
print(df['Quantity'].max())
df.info()

### 
```
### 
# ✅ Results
- Missing values filled appropriately
- Outliers corrected based on category logic
- Dataset ready for AI analysis or reporting
- Maintained data integrity and accuracy

### 🧰 Tools & Technologies
- Python 3.x
- Pandas
- NumPy
- Jupyter Notebook (optional for exploration)

### 🔍 Fiverr Research Insights
- Missing numerical values handled with median or mean
- Categorical missing values handled with mode or default values
- Outliers capped using IQR method or category mean
- Emphasis on preserving data integrity and reporting changes

### 📁 Project Structure
AlphaDay2_DataSurgeon/
│
├── data/
│   ├── broken_sales_data.csv
│   └── cleaned_sales_data.csv
├── scripts/
│   └── AlphaDay2_DataSurgeon.py
├── research/
│   └── Fiverr_Research.txt
├── README.md
└── requirements.txt
