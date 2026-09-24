import pandas as pd

# Load the raw dataset
file_path = "data/retail_store_inventory.csv"
df = pd.read_csv(file_path)

# Display basic information
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where Date could not be converted
df = df.dropna(subset=["Date"])

# Clean column names
df.columns = df.columns.str.strip()

# Save cleaned dataset
output_path = "data/retail_store_inventory_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nCleaning completed successfully!")
print("Cleaned dataset shape:", df.shape)
print("Saved as:", output_path)
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
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load cleaned dataset
file_path = "data/retail_store_inventory_cleaned.csv"
df = pd.read_csv(file_path)

# Select features and target
X = df[[
    "Inventory Level",
    "Units Ordered",
    "Price",
    "Discount",
    "Competitor Pricing"
]]

y = df["Units Sold"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("Demand Prediction Model")
print("-----------------------")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)

print("\nModel completed successfully!")
import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Inventory Demand Intelligence",
    page_icon="📦",
    layout="wide"
)

# Load data
file_path = "data/retail_store_inventory_cleaned.csv"
df = pd.read_csv(file_path)

# Title
st.title("📦 Inventory Demand Prediction & Stock Optimization")
st.write("Business Intelligence Dashboard for Inventory and Demand Analysis")

# -------------------------------
# Key Performance Indicators
# -------------------------------
total_units_sold = df["Units Sold"].sum()
avg_inventory = df["Inventory Level"].mean()
avg_demand = df["Demand Forecast"].mean()
avg_units_sold = df["Units Sold"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Units Sold", f"{total_units_sold:,.0f}")
col2.metric("Average Inventory", f"{avg_inventory:,.1f}")
col3.metric("Average Demand Forecast", f"{avg_demand:,.1f}")
col4.metric("Average Units Sold", f"{avg_units_sold:,.1f}")

# -------------------------------
# Sales by Category
# -------------------------------
st.subheader("Sales by Category")

category_sales = (
    df.groupby("Category")["Units Sold"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)

# -------------------------------
# Sales by Region
# -------------------------------
st.subheader("Sales by Region")

region_sales = (
    df.groupby("Region")["Units Sold"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_sales)

# -------------------------------
# Demand Forecast vs Actual
# -------------------------------
st.subheader("Demand Forecast vs Actual Sales")

comparison = pd.DataFrame({
    "Demand Forecast": [df["Demand Forecast"].mean()],
    "Actual Units Sold": [df["Units Sold"].mean()]
})

st.bar_chart(comparison.T)

# -------------------------------
# Inventory Risk
# -------------------------------
df["Inventory Gap"] = (
    df["Inventory Level"] - df["Demand Forecast"]
)

low_inventory = (df["Inventory Gap"] < 0).sum()
high_inventory = (df["Inventory Gap"] > 100).sum()

st.subheader("Inventory Risk")

risk_col1, risk_col2 = st.columns(2)

risk_col1.metric(
    "Potential Low-Inventory Records",
    f"{low_inventory:,}"
)

risk_col2.metric(
    "High-Inventory Records",
    f"{high_inventory:,}"
)

st.success("Dashboard loaded successfully!")
