import pandas as pd

# Read the CSV file
df = pd.read_csv("data_tamrin1.csv", encoding="utf-8")

# Convert columns to numeric in case they are stored as text
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")

# Calculate mean
mean_age = df["Age"].mean()
mean_weight = df["Weight"].mean()

# Calculate median
median_age = df["Age"].median()
median_weight = df["Weight"].median()

# Calculate mode (first mode in case of multiple)
mode_height = df["Height"].mode().iloc[0]
mode_gender = df["Gender"].mode().iloc[0]
mode_education = df["Education"].mode().iloc[0]

# Calculate range (max - min)
age_range = df["Age"].max() - df["Age"].min()
height_range = df["Height"].max() - df["Height"].min()
weight_range = df["Weight"].max() - df["Weight"].min()

# Calculate variance and standard deviation
age_variance = df["Age"].var()
age_std = df["Age"].std()

height_variance = df["Height"].var()
height_std = df["Height"].std()

weight_variance = df["Weight"].var()
weight_std = df["Weight"].std()

# Calculate quartiles
age_q1 = df["Age"].quantile(0.25)
age_q2 = df["Age"].quantile(0.50)
age_q3 = df["Age"].quantile(0.75)

height_q1 = df["Height"].quantile(0.25)
height_q2 = df["Height"].quantile(0.50)
height_q3 = df["Height"].quantile(0.75)

weight_q1 = df["Weight"].quantile(0.25)
weight_q2 = df["Weight"].quantile(0.50)
weight_q3 = df["Weight"].quantile(0.75)

# Calculate IQR (Q3 - Q1)
age_iqr = age_q3 - age_q1
height_iqr = height_q3 - height_q1
weight_iqr = weight_q3 - weight_q1

# Print results
print("Age mean:", mean_age)
print("Age median:", median_age)
print("Weight mean:", mean_weight)
print("Weight median:", median_weight)
print("Height mode:", mode_height)
print("Gender mode:", mode_gender)
print("Education mode:", mode_education)
print("Age range:", age_range)
print("Height range:", height_range)
print("Weight range:", weight_range)
print("Age variance:", age_variance)
print("Age standard deviation:", age_std)
print("Height variance:", height_variance)
print("Height standard deviation:", height_std)
print("Weight variance:", weight_variance)
print("Weight standard deviation:", weight_std)
print("Age Q1:", age_q1)
print("Age Q2 (Median):", age_q2)
print("Age Q3:", age_q3)
print("Height Q1:", height_q1)
print("Height Q2 (Median):", height_q2)
print("Height Q3:", height_q3)
print("Weight Q1:", weight_q1)
print("Weight Q2 (Median):", weight_q2)
print("Weight Q3:", weight_q3)
print("Age IQR:", age_iqr)
print("Height IQR:", height_iqr)
print("Weight IQR:", weight_iqr)