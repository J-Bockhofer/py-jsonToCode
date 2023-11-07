class L_1_5_1:
    def __init__(self, user:str, rating:int, comment:str):
        self.user = user
        self.rating = rating
        self.comment = comment
    def to_dict(self)->dict:
        return {"user": self.user, "rating": self.rating, "comment": self.comment}
    @classmethod
    def from_dict(cls, data:dict):
        if "user" in data and "rating" in data and "comment" in data:
            return cls(data["user"], data["rating"], data["comment"])
        else:
            raise KeyError("Invalid data for L_1_5_1")
class L_0_2_1:
    def __init__(self, product_id:str, name:str, description:str, price:float, quantity:int, reviews:list[L_1_5_1]):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.reviews = reviews
    def to_dict(self)->dict:
        return {"product_id": self.product_id, "name": self.name, "description": self.description, "price": self.price, "quantity": self.quantity, "reviews": [x.to_dict() for x in self.reviews]}
    @classmethod
    def from_dict(cls, data:dict):
        if "product_id" in data and "name" in data and "description" in data and "price" in data and "quantity" in data and "reviews" in data:
            classlist_reviews = [L_1_5_1.from_dict(classdata) for classdata in data.get("reviews", [])]
            return cls(data["product_id"], data["name"], data["description"], data["price"], data["quantity"], classlist_reviews)
        else:
            raise KeyError("Invalid data for L_0_2_1")
class L_1_2_1:
    def __init__(self, product_id:str, quantity:int):
        self.product_id = product_id
        self.quantity = quantity
    def to_dict(self)->dict:
        return {"product_id": self.product_id, "quantity": self.quantity}
    @classmethod
    def from_dict(cls, data:dict):
        if "product_id" in data and "quantity" in data:
            return cls(data["product_id"], data["quantity"])
        else:
            raise KeyError("Invalid data for L_1_2_1")
class L_0_3_1:
    def __init__(self, order_id:str, customer_name:str, items:list[L_1_2_1], total_price:float, order_date:str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_price = total_price
        self.order_date = order_date
    def to_dict(self)->dict:
        return {"order_id": self.order_id, "customer_name": self.customer_name, "items": [x.to_dict() for x in self.items], "total_price": self.total_price, "order_date": self.order_date}
    @classmethod
    def from_dict(cls, data:dict):
        if "order_id" in data and "customer_name" in data and "items" in data and "total_price" in data and "order_date" in data:
            classlist_items = [L_1_2_1.from_dict(classdata) for classdata in data.get("items", [])]
            return cls(data["order_id"], data["customer_name"], classlist_items, data["total_price"], data["order_date"])
        else:
            raise KeyError("Invalid data for L_0_3_1")
class L_0:
    def __init__(self, store:str, location:str, inventory:list[L_0_2_1], orders:list[L_0_3_1]):
        self.store = store
        self.location = location
        self.inventory = inventory
        self.orders = orders
    def to_dict(self)->dict:
        return {"store": self.store, "location": self.location, "inventory": [x.to_dict() for x in self.inventory], "orders": [x.to_dict() for x in self.orders]}
    @classmethod
    def from_dict(cls, data:dict):
        if "store" in data and "location" in data and "inventory" in data and "orders" in data:
            classlist_inventory = [L_0_2_1.from_dict(classdata) for classdata in data.get("inventory", [])]
            classlist_orders = [L_0_3_1.from_dict(classdata) for classdata in data.get("orders", [])]
            return cls(data["store"], data["location"], classlist_inventory, classlist_orders)
        else:
            raise KeyError("Invalid data for L_0")
