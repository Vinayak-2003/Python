import pandas as pd

# Example JSON data
json_data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]

# Convert JSON to DataFrame
df = pd.DataFrame(json_data)

# Save DataFrame to Excel
output_file = "output.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"JSON data has been successfully written to {output_file}")
