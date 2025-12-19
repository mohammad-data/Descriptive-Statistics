import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("data.csv", encoding="utf-8")

# List of monthly income columns
months = ["January income", "February income", "March income", "April income",
          "May income", "June income", "July income", "August income",
          "September income", "October income", "November income", "December income"]

# Convert income columns to numeric
for month in months:
    df[month] = pd.to_numeric(df[month], errors="coerce")

# Calculate average income for each person
df["Average Income"] = df[months].mean(axis=1)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(df["Name"], df["Average Income"], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Average Income")
plt.title("Average Income per Person")
plt.tight_layout()
plt.show()
#---------------------------------------------------------------------------------------
# Plot line chart for income trend
plt.figure(figsize=(12,6))

for i, row in df.iterrows():
    plt.plot(months, row[months], marker='o', label=row["Name"])

plt.xticks(rotation=45)
plt.ylabel("Income")
plt.title("Monthly Income Trend per Person")
plt.legend()
plt.tight_layout()
plt.show()