import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path = "data/retail_store_inventory_cleaned.csv"
df = pd.read_csv(file_path)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Basic information
print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

# -------------------------------
# 1. Total Units Sold
# -------------------------------
total_units_sold = df["Units Sold"].sum()
print("\nTotal Units Sold:", total_units_sold)

# -------------------------------
# 2. Sales by Category
# -------------------------------
category_sales = df.groupby("Category")["Units Sold"].sum().sort_values(ascending=False)

print("\nUnits Sold by Category:")
print(category_sales)

category_sales.plot(kind="bar", title="Units Sold by Category")
plt.xlabel("Category")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

# -------------------------------
# 3. Sales by Region
# -------------------------------
region_sales = df.groupby("Region")["Units Sold"].sum().sort_values(ascending=False)

print("\nUnits Sold by Region:")
print(region_sales)

region_sales.plot(kind="bar", title="Units Sold by Region")
plt.xlabel("Region")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.close()

# -------------------------------
# 4. Sales Trend Over Time
# -------------------------------
daily_sales = df.groupby("Date")["Units Sold"].sum()

print("\nAverage Daily Units Sold:", daily_sales.mean())

daily_sales.plot(title="Daily Units Sold Trend")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("daily_sales_trend.png")
plt.close()

# -------------------------------
# 5. Inventory vs Units Sold
# -------------------------------
print("\nAverage Inventory Level:", df["Inventory Level"].mean())
print("Average Units Sold:", df["Units Sold"].mean())
print("Average Units Ordered:", df["Units Ordered"].mean())

# -------------------------------
# EDA Completed
# -------------------------------
print("\nEDA completed successfully!")
print("Charts saved:")
print("- category_sales.png")
print("- region_sales.png")
print("- daily_sales_trend.png")

# -------------------------------
# 6. Demand Forecast vs Actual Sales
# -------------------------------
forecast_comparison = df[
    ["Demand Forecast", "Units Sold"]
].mean()

print("\nAverage Demand Forecast:", forecast_comparison["Demand Forecast"])
print("Average Actual Units Sold:", forecast_comparison["Units Sold"])

forecast_gap = (
    df["Demand Forecast"] - df["Units Sold"]
).mean()

print("Average Forecast Gap:", forecast_gap)

# -------------------------------
# 7. Inventory vs Demand
# -------------------------------
inventory_demand = df[
    ["Inventory Level", "Demand Forecast", "Units Sold"]
].mean()

print("\nAverage Inventory Level:", inventory_demand["Inventory Level"])
print("Average Demand Forecast:", inventory_demand["Demand Forecast"])
print("Average Units Sold:", inventory_demand["Units Sold"])

# -------------------------------
# 8. Potential Stock Risk
# -------------------------------
df["Inventory Gap"] = (
    df["Inventory Level"] - df["Demand Forecast"]
)

print("\nAverage Inventory Gap:", df["Inventory Gap"].mean())

high_inventory = (df["Inventory Gap"] > 100).sum()
low_inventory = (df["Inventory Gap"] < 0).sum()

print("Records with high inventory:", high_inventory)
print("Records with potential low inventory:", low_inventory)