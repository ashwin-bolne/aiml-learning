import pandas as pd


df = pd.read_csv("data/house_prices.csv")

print(df.head())

print(f"\nDataset Shape: {df.shape}")

print(f"\nDataset columns: {df.columns}")

print(f"\nDataset Data Types: \n{df.dtypes}")

print(f"\nStastical Summary: \n{df.describe()}")

missing_values = df.isnull().sum()

missing_values = missing_values[missing_values > 0]

missing_values = missing_values.sort_values(
    ascending = False 
)

print(f"\nColumns With Missing Values: \n{missing_values}")

target_col = "SalePrice"
y = df[target_col]

print(f"\nTarget variable summary: \n{y.describe()}")