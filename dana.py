import pandas as pd

# Load the Excel file
file_path = "input_file.xlsx"
df = pd.read_excel(file_path)

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
    writer = pd.ExcelWriter(file_path, engine='openpyxl')
    writer.book = pd.ExcelFile(file_path)  # type: ignore
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    writer.save()  # type: ignore

# Save the modified DataFrame back to the Excel file
# df.to_excel("output_file.xlsx", index=False)

print("Negative numbers in all columns have been replaced with 'ND'.")
