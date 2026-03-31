import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("C:/Users/prani/Downloads/IMDB_Synthetic_Dataset.csv")
# -------------------------------
# 1. Handling Missing Values
print("\nMissing Values:\n")
print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].mean())   # numerical → mean
    else:
        df[col] = df[col].fillna(df[col].mode()[0])  # categorical → mode
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
# 3. Boxplot
plt.boxplot([df['IMDB_Rating'], df['Votes']])

plt.xticks([1, 2], ['IMDB Rating', 'Votes'])
plt.title("Boxplot Comparison")

plt.show()