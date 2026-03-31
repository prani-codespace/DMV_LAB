# Step 1: Import library
import pandas as pd

# Step 2: Create sample dataset (you can replace this with CSV file)
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [20, None, 22, None, 25],
    'City': ['Kolkata', 'Delhi', None, 'Mumbai', None],
    'Salary': [30000, 40000, None, 50000, None]
}

df = pd.DataFrame(data)

# Step 3: Display original data
print("Original Data:\n")
print(df)

# Step 4: Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Step 5: Fill missing values

# Fill numerical columns with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Fill categorical column with mode
df['City'] = df['City'].fillna(df['City'].mode()[0])

# Step 6: Display updated data
print("\nData after handling missing values:\n")
print(df)

# Step 7: Optional - Drop rows if still any missing
df = df.dropna()

# Final output
print("\nFinal Clean Data:\n")
print(df)