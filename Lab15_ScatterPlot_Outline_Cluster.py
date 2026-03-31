import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("IMDB_Synthetic_Dataset.csv")

# -------------------------------
# 1. Handle missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)
# -------------------------------
# 2. Outliner 
Q1 = df['IMDB_Rating'].quantile(0.25)
Q3 = df['IMDB_Rating'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['IMDB_Rating'] < lower) | (df['IMDB_Rating'] > upper)]
print(outliers)
# -------------------------------
# 3. Scatter Plot

# Main data (cluster + correlation)
x = df['Votes']
y = df['IMDB_Rating']

plt.scatter(x, y)

# Add OUTLIERS manually
plt.scatter([1000000, 50], [1, 9])

plt.title("Scatter Plot: Votes vs IMDB Rating")
plt.xlabel("Votes")
plt.ylabel("IMDB Rating")

plt.show()