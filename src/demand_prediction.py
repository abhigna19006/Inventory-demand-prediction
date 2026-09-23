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