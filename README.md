# Product Inventory Parser & Reporter

A Python-based tool designed to parse, validate, and merge product inventory data from raw text files. It handles messy formatting, detects data conflicts, and generates clean CSV reports.

- **Parsing**: Handles multiple delimiters (`:` and `=`) and cleans currency strings (e.g., "55 Euro").
- **Data Merging**: Automatically combines quantities for duplicate products if their stock status matches.
- **Conflict Detection**: Flags items with the same name but different "Out of Stock" statuses as errors.
- **Robust Error Handling**: Captures malformed lines (invalid numbers, missing keys) without crashing.
- **Dual Reporting**: 
  - `inventory_report.csv`: Clean, sorted, and merged data.
  - `failed_imports.csv`: Log of skipped lines with specific error reasons.

## Project Structure
- `main.py`: The entry point.
- `reader.py`: Contains the logic for file I/O, parsing, and the merging algorithm.
- `product.py`: The `Product` class (OOP Model) defining data structure and CSV formatting.
- `products.txt`: The source data file (ignored by Git).

## Input Format Example
The parser expects lines in the following format:
`product_name: T-shirt ; quantity = 78 ; price: 55 Euro; out of stock : YES`

## How to Use
1. Place your data in a file named `products.txt` in the root directory.
2. Run the main script:
   ```bash
   python main.py
