"""
Alpha Day 2 – Data Surgeon
Objective: Clean broken_sales_data.csv
Author: Wajiha
"""

import pandas as pd
import os


# --------------------------------------------------
# 1. Check Working Directory
# --------------------------------------------------
print("Current Working Directory:", os.getcwd())


# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------
df = pd.read_csv("broken_sales_data.csv")

print("\nRaw Data:")
print(df)


# --------------------------------------------------
# 3. Detect Missing Values
# --------------------------------------------------
print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 4. Fill Missing Sales (Electronics Category)
# --------------------------------------------------
electronics_median = df[df["Category"] == "Electronics"]["Sales"].median()

df.loc[df["Category"] == "Electronics", "Sales"] = \
    df.loc[df["Category"] == "Electronics", "Sales"].fillna(electronics_median)


# --------------------------------------------------
# 5. Fill Missing Quantity (Chair = 1)
# --------------------------------------------------
df.loc[df["Product"] == "Chair", "Quantity"] = \
    df.loc[df["Product"] == "Chair", "Quantity"].fillna(1)


# --------------------------------------------------
# 6. Handle Outliers (Quantity > 100)
# --------------------------------------------------
OUTLIER_THRESHOLD = 100

office_mean_quantity = df[df["Category"] == "Office"]["Quantity"].mean()

df.loc[df["Quantity"] > OUTLIER_THRESHOLD, "Quantity"] = office_mean_quantity


# --------------------------------------------------
# 7. Final Verification
# --------------------------------------------------
print("\nFinal Dataset:")
print(df)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nData Info:")
print(df.info())


# --------------------------------------------------
# 8. Save Cleaned Dataset
# --------------------------------------------------
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully.")