import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
print("Average age:", df["Age"].mean())
