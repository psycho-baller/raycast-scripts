import pandas as pd

# Load the Excel file
file_path = "input.xlsx"
# Load all sheets in the Excel file into a dictionary of DataFrames
dfs = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')
writer = pd.ExcelWriter(file_path, engine='openpyxl')

# Loop through all sheets
for sheet_name, df in dfs.items():
    # Loop through all cells in the DataFrame
    for index, row in df.iterrows():
        for column_name in df.columns:
            value = row[column_name]
            # Check if the value is numeric
            if pd.api.types.is_numeric_dtype(pd.Series(value)):
                # Replace negative numbers with "ND"
                if value < 0:
                    df.at[index, column_name] = "ND"

    # Save the modified DataFrame back to the sheet
    df.to_excel(writer, sheet_name=sheet_name, index=False)
writer.close()

print("Negative numbers in all columns have been replaced with 'ND'.")
