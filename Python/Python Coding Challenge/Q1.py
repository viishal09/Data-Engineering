import pandas as pd

# Reading CSV data into a Pandas DataFrame
df = pd.read_csv('example.csv')

# Displaying the DataFrame
print("Display Dataframe ---")
print(df)

# Filtering data using the query method
filtered_df = df.query('Salary > 50000')

# Displaying the filtered DataFrame
print("Display Filtered Dataframe ---")
print(filtered_df)
