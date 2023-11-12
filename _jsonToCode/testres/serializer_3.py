class Reviews:
    def __init__(self, user:str, rating:int, comment:str):
        self.user = user
        self.rating = rating
        self.comment = comment
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Reviews: user = {self.user.__str__()}, rating = {self.rating.__str__()}, comment = {self.comment.__str__()}'
    def __repr__(self):
        return f'Reviews(user={repr(self.user)}, rating={repr(self.rating)}, comment={repr(self.comment)})'
    def to_dict(self)->dict:
        return {"user": self.user, "rating": self.rating, "comment": self.comment}
    @classmethod
    def from_dict(cls, data:dict)->'Reviews':
        if "user" in data and "rating" in data and "comment" in data:
            return cls(data["user"], data["rating"], data["comment"])
        else:
            raise KeyError("Invalid data for Reviews")
class Inventory:
    def __init__(self, product_id:str, name:str, description:str, price:float, quantity:int, reviews:list[Reviews]):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.reviews = reviews
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Inventory: product_id = {self.product_id.__str__()}, name = {self.name.__str__()}, description = {self.description.__str__()}, price = {self.price.__str__()}, quantity = {self.quantity.__str__()}, reviews = {[x.__str__() for x in self.reviews]}'
    def __repr__(self):
        return f'Inventory(product_id={repr(self.product_id)}, name={repr(self.name)}, description={repr(self.description)}, price={repr(self.price)}, quantity={repr(self.quantity)}, reviews={repr(self.reviews)})'
    def to_dict(self)->dict:
        return {"product_id": self.product_id, "name": self.name, "description": self.description, "price": self.price, "quantity": self.quantity, "reviews": [x.to_dict() for x in self.reviews]}
    @classmethod
    def from_dict(cls, data:dict)->'Inventory':
        if "product_id" in data and "name" in data and "description" in data and "price" in data and "quantity" in data and "reviews" in data:
            classlist_reviews = [Reviews.from_dict(classdata) for classdata in data.get("reviews", [])]
            return cls(data["product_id"], data["name"], data["description"], data["price"], data["quantity"], classlist_reviews)
        else:
            raise KeyError("Invalid data for Inventory")
class Items:
    def __init__(self, product_id:str, quantity:int):
        self.product_id = product_id
        self.quantity = quantity
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Items: product_id = {self.product_id.__str__()}, quantity = {self.quantity.__str__()}'
    def __repr__(self):
        return f'Items(product_id={repr(self.product_id)}, quantity={repr(self.quantity)})'
    def to_dict(self)->dict:
        return {"product_id": self.product_id, "quantity": self.quantity}
    @classmethod
    def from_dict(cls, data:dict)->'Items':
        if "product_id" in data and "quantity" in data:
            return cls(data["product_id"], data["quantity"])
        else:
            raise KeyError("Invalid data for Items")
class Orders:
    def __init__(self, order_id:str, customer_name:str, items:list[Items], total_price:float, order_date:str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_price = total_price
        self.order_date = order_date
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Orders: order_id = {self.order_id.__str__()}, customer_name = {self.customer_name.__str__()}, items = {[x.__str__() for x in self.items]}, total_price = {self.total_price.__str__()}, order_date = {self.order_date.__str__()}'
    def __repr__(self):
        return f'Orders(order_id={repr(self.order_id)}, customer_name={repr(self.customer_name)}, items={repr(self.items)}, total_price={repr(self.total_price)}, order_date={repr(self.order_date)})'
    def to_dict(self)->dict:
        return {"order_id": self.order_id, "customer_name": self.customer_name, "items": [x.to_dict() for x in self.items], "total_price": self.total_price, "order_date": self.order_date}
    @classmethod
    def from_dict(cls, data:dict)->'Orders':
        if "order_id" in data and "customer_name" in data and "items" in data and "total_price" in data and "order_date" in data:
            classlist_items = [Items.from_dict(classdata) for classdata in data.get("items", [])]
            return cls(data["order_id"], data["customer_name"], classlist_items, data["total_price"], data["order_date"])
        else:
            raise KeyError("Invalid data for Orders")
class Root:
    def __init__(self, store:str, location:str, inventory:list[Inventory], orders:list[Orders]):
        self.store = store
        self.location = location
        self.inventory = inventory
        self.orders = orders
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Root: store = {self.store.__str__()}, location = {self.location.__str__()}, inventory = {[x.__str__() for x in self.inventory]}, orders = {[x.__str__() for x in self.orders]}'
    def __repr__(self):
        return f'Root(store={repr(self.store)}, location={repr(self.location)}, inventory={repr(self.inventory)}, orders={repr(self.orders)})'
    def to_dict(self)->dict:
        return {"store": self.store, "location": self.location, "inventory": [x.to_dict() for x in self.inventory], "orders": [x.to_dict() for x in self.orders]}
    @classmethod
    def from_dict(cls, data:dict)->'Root':
        if "store" in data and "location" in data and "inventory" in data and "orders" in data:
            classlist_inventory = [Inventory.from_dict(classdata) for classdata in data.get("inventory", [])]
            classlist_orders = [Orders.from_dict(classdata) for classdata in data.get("orders", [])]
            return cls(data["store"], data["location"], classlist_inventory, classlist_orders)
        else:
            raise KeyError("Invalid data for Root")
