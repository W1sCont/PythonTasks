# Міні-магазин

# Класи: Product, Cart, Store
# Ідея:

# Store: містить товари.

# Cart: додавання/видалення товарів, підрахунок суми.

# Всього кілька товарів + можливість купівлі.

class Product:
    def __init__(self, product: str, cost: int):
        self.product = product
        self.cost = cost

    def __str__(self):
        return f"{self.product} - {self.cost} грн"

class Cart:
    def __init__(self):
        self.card = []
    
    def add_product(self, product: Product):
        self.card.append(product)

    def remove_product(self, product: Product):
        self.card.remove(product)

    def all_products(self):
        for i, el in enumerate(self.card, 1):
            print(f"{i}. {el}")

    def get_total(self):
        result = sum(item.cost for item in self.card)
        return print(f"В кошику товар вартістю: {result} грн")


class Store:
    def __init__(self):
        self.cart = Cart()

    def 


banan = Product("banan", 10)
pomelo = Product("Pomelo", 12)
cart_1 = Cart()
cart_1.add_product(banan)
cart_1.add_product(pomelo)
cart_1.all_products()
cart_1.get_total()

