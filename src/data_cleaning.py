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