# Data Pipeline for Customer and Order Data

This project implements a modular ETL pipeline designed to process and transform multiple data sources for customer and e-commerce workflows. The pipeline automates data ingestion, file pattern detection, dynamic metadata extraction from filenames, and structured output generation for downstream use.

## 📁 Input Files

The pipeline is configured to process the following types of files located in a unified data staging layer:

| File Type               | Pattern Example                      | Transformation Logic                        |
|------------------------|---------------------------------------|---------------------------------------------|
| Customer Master         | CUST_MSTR_YYYYMMDD.csv                | Extracts date from filename → adds `date` column |
| Master-Child Export     | master_child_export-YYYYMMDD.csv      | Extracts date & date_key from filename      |
| E-commerce Order Header | H_ECOM_ORDER.csv                      | Loaded as-is without transformation         |

> Multiple dated versions of CUST_MSTR and master_child_export files are supported.

---

## ⚙️ Pipeline Features

- ✅ Scans and processes all matching files dynamically
- 📅 Automatically extracts and adds metadata from filenames (date, date_key)
- 📂 Writes clean structured CSVs to a designated output layer for further use

---

## 🔄 Processing Logic

Each file type undergoes a structured transformation:

### 1. Customer Master (CUST_MSTR_YYYYMMDD.csv)
- Adds a column `date` in `YYYY-MM-DD` format based on filename.

### 2. Master-Child Export (master_child_export-YYYYMMDD.csv)
- Adds two columns:
  - `date`: Parsed as `YYYY-MM-DD`
  - `date_key`: Parsed as `YYYYMMDD` integer

---

## 🛠️ Technologies Used

- Python 3.x
- pandas (for data handling)
- Built-in datetime and os modules

---

## 🚀 Running the Pipeline

1. Place all input files in the same folder as the script (or configure path in code)
2. Run the script:

```bash
python etl_clean_files.py
