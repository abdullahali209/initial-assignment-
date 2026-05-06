import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Show first 5 rows
print(df.head())

# Basic statistics
print(df.describe())

# Plot Closing Price
plt.plot(df["Close"])
plt.title("Google Stock Closing Prices")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()
