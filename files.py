import os
import pandas as pd
from datetime import datetime

# Folder containing files (same as script)
folder_path = os.path.dirname(os.path.abspath(__file__))

# Output folder (optional)
output_path = os.path.join(folder_path, 'processed')
os.makedirs(output_path, exist_ok=True)

# Loop through files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Only process CSV files
    if not filename.endswith(".csv"):
        continue

    if filename.startswith("CUST_MSTR_"):
        date_str = filename.split("_")[2].split(".")[0]
        date_formatted = datetime.strptime(date_str, "%Y%m%d").strftime('%Y-%m-%d')
        df = pd.read_csv(file_path)
        df['date'] = date_formatted
        output_file = os.path.join(output_path, f"clean_{filename}")
        df.to_csv(output_file, index=False)
        print(f"✅ Processed {filename} → {output_file}")

    elif filename.startswith("master_child_export-"):
        date_str = filename.split("-")[1].split(".")[0]
        date = datetime.strptime(date_str, "%Y%m%d").strftime('%Y-%m-%d')
        date_key = int(date_str)
        df = pd.read_csv(file_path)
        df['date'] = date
        df['date_key'] = date_key
        output_file = os.path.join(output_path, f"clean_{filename}")
        df.to_csv(output_file, index=False)
        print(f"✅ Processed {filename} → {output_file}")

    elif filename.startswith("H_ECOM_ORDER"):
        df = pd.read_csv(file_path)
        output_file = os.path.join(output_path, f"clean_{filename}")
        df.to_csv(output_file, index=False)
        print(f"✅ Copied {filename} → {output_file}")
