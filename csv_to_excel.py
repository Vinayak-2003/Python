import pandas as pd
import chardet

csv_file = "commits.csv"

# Detect encoding
with open(csv_file, "rb") as f:
    result = chardet.detect(f.read())
    encoding = result["encoding"]

# Read CSV using detected encoding
data = pd.read_csv(csv_file, names=["Commit Hash", "Author", "Date"], encoding=encoding)
data.to_excel("commits.xlsx", index=False)

print("Completed")
