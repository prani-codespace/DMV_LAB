import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("IMDB_Synthetic_Dataset.csv")
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
# 3. Bar Chart (Insight: Most common genres)
genre_counts = df['Genre'].value_counts().head(10)
genre_counts.plot(kind='bar',color="Green")
plt.title("Top Genres Distribution")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()
# -------------------------------
# 4. Histogram (Insight: Rating distribution)
df['IMDB_Rating'].plot(kind='hist', bins=10,color="Green")
plt.title("IMDB Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()
# -------------------------------
# 5. Line Chart (Insight: Trend over years)
yearly_avg = df.groupby('Release_Year')['IMDB_Rating'].mean()
yearly_avg.plot(kind='line',color="yellow")
plt.title("Average Rating Over Years")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.show()
# -------------------------------
# 6. Scatter Plot (Insight: Votes vs Rating)
plt.scatter(df['Votes'], df['IMDB_Rating'],color="Green")
plt.title("Votes vs Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")
plt.show()
# -------------------------------
# 7. Pie Chart (Insight: Genre share)
top_genres = df['Genre'].value_counts().head(5)
top_genres.plot(kind='pie', autopct='%1.1f%%')
plt.title("Top 5 Genre Share")
plt.ylabel("") 
plt.show()
