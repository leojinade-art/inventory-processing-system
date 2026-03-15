import csv
from pathlib import Path
from product import Product

def read_products(filename="products.txt"):
    valid_registry = {}
    invalid_lines = []

    file_path = Path(__file__).parent / filename
    if not file_path.exists(): return [], []

    with open(file_path, "r") as f:
        for i, line in enumerate(f, 1):
            clean_line = line.strip()
            if not clean_line: continue

            try:
                parts = clean_line.replace('=', ':').split(';')
                data = {}
                for p in parts:
                    k, v = p.split(':', 1)
                    data[k.strip().lower()] = v.strip().lower()

                name = data['product_name'].title()
                qty = int(data['quantity'].split(',')[0].strip())
                price = float(data['price'].replace('euro', '').strip())
                is_out = data['out of stock'] == "yes"

                if name in valid_registry:
                    existing = valid_registry[name]
                    if existing.out_of_stock == is_out:
                        existing.quantity += qty
                        existing.price = price 
                    else:
                        invalid_lines.append([i, clean_line, "Status Conflict (In vs Out)"])
                else:
                    valid_registry[name] = Product(name, qty, price, is_out)

            except (ValueError, KeyError, IndexError) as e:
                invalid_lines.append([i, clean_line, f"Formatting Error: {str(e)}"])
                
    return list(valid_registry.values()), invalid_lines

def save_reports(valid, invalid):
    path = Path(__file__).parent
    
    with open(path / "inventory_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Product Name", "Total Quantity", "Price", "Out of Stock"])
        writer.writerows([p.to_row() for p in valid])

    with open(path / "failed_imports.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Line", "Content", "Reason"])
        writer.writerows(invalid)
