import random
import string

class Review:
    """
        Review:
        def __init__(self, user:str, rating:int, comment:str)
    """
    def __init__(self, user:str, rating:int, comment:str):
        self.user = user
        self.rating = rating
        self.comment = comment
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Review: user = {self.user.__str__()}, rating = {self.rating.__str__()}, comment = {self.comment.__str__()}'
    def __repr__(self):
        return f'Review(user={repr(self.user)}, rating={repr(self.rating)}, comment={repr(self.comment)})'
    def to_dict(self)->dict:
        return {"user": self.user, "rating": self.rating, "comment": self.comment}
    @classmethod
    def from_dict(cls, data:dict)->'Review':
        if "user" in data and "rating" in data and "comment" in data:
            return cls(data["user"], data["rating"], data["comment"])
        else:
            raise KeyError("Invalid data for Review")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Review':
        if seed:
            random.seed(seed)
        user = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        rating = random.randint(lowlim, uplim)
        comment = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(user, rating, comment)
class Inventory:
    """
        Inventory:
        def __init__(self, product_id:str, name:str, description:str, price:float, quantity:int, reviews:list[Review])
    """
    def __init__(self, product_id:str, name:str, description:str, price:float, quantity:int, reviews:list[Review]):
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
            classlist_reviews = [Review.from_dict(classdata) for classdata in data.get("reviews", [])]
            return cls(data["product_id"], data["name"], data["description"], data["price"], data["quantity"], classlist_reviews)
        else:
            raise KeyError("Invalid data for Inventory")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Inventory':
        if seed:
            random.seed(seed)
        product_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        description = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        price = random.uniform(lowlim, uplim)
        quantity = random.randint(lowlim, uplim)
        reviews = [Review.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(product_id, name, description, price, quantity, reviews)
class Item:
    """
        Item:
        def __init__(self, product_id:str, quantity:int)
    """
    def __init__(self, product_id:str, quantity:int):
        self.product_id = product_id
        self.quantity = quantity
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Item: product_id = {self.product_id.__str__()}, quantity = {self.quantity.__str__()}'
    def __repr__(self):
        return f'Item(product_id={repr(self.product_id)}, quantity={repr(self.quantity)})'
    def to_dict(self)->dict:
        return {"product_id": self.product_id, "quantity": self.quantity}
    @classmethod
    def from_dict(cls, data:dict)->'Item':
        if "product_id" in data and "quantity" in data:
            return cls(data["product_id"], data["quantity"])
        else:
            raise KeyError("Invalid data for Item")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Item':
        if seed:
            random.seed(seed)
        product_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        quantity = random.randint(lowlim, uplim)
        return cls(product_id, quantity)
class Order:
    """
        Order:
        def __init__(self, order_id:str, customer_name:str, items:list[Item], total_price:float, order_date:str)
    """
    def __init__(self, order_id:str, customer_name:str, items:list[Item], total_price:float, order_date:str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_price = total_price
        self.order_date = order_date
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Order: order_id = {self.order_id.__str__()}, customer_name = {self.customer_name.__str__()}, items = {[x.__str__() for x in self.items]}, total_price = {self.total_price.__str__()}, order_date = {self.order_date.__str__()}'
    def __repr__(self):
        return f'Order(order_id={repr(self.order_id)}, customer_name={repr(self.customer_name)}, items={repr(self.items)}, total_price={repr(self.total_price)}, order_date={repr(self.order_date)})'
    def to_dict(self)->dict:
        return {"order_id": self.order_id, "customer_name": self.customer_name, "items": [x.to_dict() for x in self.items], "total_price": self.total_price, "order_date": self.order_date}
    @classmethod
    def from_dict(cls, data:dict)->'Order':
        if "order_id" in data and "customer_name" in data and "items" in data and "total_price" in data and "order_date" in data:
            classlist_items = [Item.from_dict(classdata) for classdata in data.get("items", [])]
            return cls(data["order_id"], data["customer_name"], classlist_items, data["total_price"], data["order_date"])
        else:
            raise KeyError("Invalid data for Order")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Order':
        if seed:
            random.seed(seed)
        order_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        customer_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        items = [Item.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        total_price = random.uniform(lowlim, uplim)
        order_date = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(order_id, customer_name, items, total_price, order_date)
class Root:
    """
        Root:
        def __init__(self, store:str, location:str, inventory:list[Inventory], orders:list[Order])
    """
    def __init__(self, store:str, location:str, inventory:list[Inventory], orders:list[Order]):
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
            classlist_orders = [Order.from_dict(classdata) for classdata in data.get("orders", [])]
            return cls(data["store"], data["location"], classlist_inventory, classlist_orders)
        else:
            raise KeyError("Invalid data for Root")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Root':
        if seed:
            random.seed(seed)
        store = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        location = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        inventory = [Inventory.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        orders = [Order.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(store, location, inventory, orders)
