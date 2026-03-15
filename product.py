class Product:
    def __init__(self, name, quantity, price, out_of_stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.out_of_stock = out_of_stock

    def to_row(self):
        status = "YES" if self.out_of_stock else "NO"
        return [self.name, self.quantity, f"{self.price} Euro", status]

    def __repr__(self):
        status = "OUT OF STOCK" if self.out_of_stock else "AVAILABLE"
        return f"{self.name.ljust(15)} | Qty: {str(self.quantity).rjust(4)} | Price: {self.price}€ | {status}"
