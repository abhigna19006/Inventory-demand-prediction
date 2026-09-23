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