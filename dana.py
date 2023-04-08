import pandas as pd

# Load the Excel file
df = pd.read_excel('input_file.xlsx')

# Find all negative numbers in the DataFrame and replace them with "ND"
df[df < 0] = "ND"

# Save the modified file
df.to_excel('output_file.xlsx', index=False)
