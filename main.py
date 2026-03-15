from reader import read_products, save_reports

def main():
    valid, invalid = read_products("products.txt")
    valid.sort(key=lambda p: (not p.out_of_stock, p.name.lower()))
    save_reports(valid, invalid)

    print(f"Inventory Processed: {len(valid)} items saved, {len(invalid)} lines failed.")

if __name__ == "__main__":
    main()
