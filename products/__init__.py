from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> 'Product':
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    # Use a list comprehension for a more concise implementation
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    # Directly return the loaded Product object
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None


def add_product(product: Product):
    # Avoid passing raw dictionaries; work directly with Product objects
    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'cost': product.cost,
        'qty': product.qty
    }
    dao.add_product(product_data)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    dao.update_qty(product_id, qty)
