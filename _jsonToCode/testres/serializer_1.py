import random
import string

class Addres:
    """
        Addres:
        def __init__(self, street:str, city:str, state:str)
    """
    def __init__(self, street:str, city:str, state:str):
        self.street = street
        self.city = city
        self.state = state
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Addres: street = {self.street.__str__()}, city = {self.city.__str__()}, state = {self.state.__str__()}'
    def __repr__(self):
        return f'Addres(street={repr(self.street)}, city={repr(self.city)}, state={repr(self.state)})'
    def to_dict(self)->dict:
        return {"street": self.street, "city": self.city, "state": self.state}
    @classmethod
    def from_dict(cls, data:dict)->'Addres':
        if "street" in data and "city" in data and "state" in data:
            return cls(data["street"], data["city"], data["state"])
        else:
            raise KeyError("Invalid data for Addres")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Addres':
        if seed:
            random.seed(seed)
        street = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        city = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        state = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(street, city, state)
class User:
    """
        User:
        def __init__(self, name:str, age:int, email:str, address:Addres, hobbies:list[str], is_active:bool)
    """
    def __init__(self, name:str, age:int, email:str, address:Addres, hobbies:list[str], is_active:bool):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.hobbies = hobbies
        self.is_active = is_active
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'User: name = {self.name.__str__()}, age = {self.age.__str__()}, email = {self.email.__str__()}, address = {self.address.__str__()}, hobbies = {[x.__str__() for x in self.hobbies]}, is_active = {self.is_active.__str__()}'
    def __repr__(self):
        return f'User(name={repr(self.name)}, age={repr(self.age)}, email={repr(self.email)}, address={repr(self.address)}, hobbies={repr(self.hobbies)}, is_active={repr(self.is_active)})'
    def to_dict(self)->dict:
        return {"name": self.name, "age": self.age, "email": self.email, "address": self.address.to_dict(), "hobbies": self.hobbies, "is_active": self.is_active}
    @classmethod
    def from_dict(cls, data:dict)->'User':
        if "name" in data and "age" in data and "email" in data and "address" in data and "hobbies" in data and "is_active" in data:
            return cls(data["name"], data["age"], data["email"], Addres.from_dict(data["address"]), data["hobbies"], data["is_active"])
        else:
            raise KeyError("Invalid data for User")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'User':
        if seed:
            random.seed(seed)
        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        age = random.randint(lowlim, uplim)
        email = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        address = Addres.from_random(seed, lowlim, uplim)
        hobbies = [''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim)) for _ in range(lowlim, uplim)]
        is_active = bool(random.getrandbits(1))
        return cls(name, age, email, address, hobbies, is_active)
class Product:
    """
        Product:
        def __init__(self, id:int, name:str, price:float)
    """
    def __init__(self, id:int, name:str, price:float):
        self.id = id
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Product: id = {self.id.__str__()}, name = {self.name.__str__()}, price = {self.price.__str__()}'
    def __repr__(self):
        return f'Product(id={repr(self.id)}, name={repr(self.name)}, price={repr(self.price)})'
    def to_dict(self)->dict:
        return {"id": self.id, "name": self.name, "price": self.price}
    @classmethod
    def from_dict(cls, data:dict)->'Product':
        if "id" in data and "name" in data and "price" in data:
            return cls(data["id"], data["name"], data["price"])
        else:
            raise KeyError("Invalid data for Product")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Product':
        if seed:
            random.seed(seed)
        id = random.randint(lowlim, uplim)
        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        price = random.uniform(lowlim, uplim)
        return cls(id, name, price)
class Root:
    """
        Root:
        def __init__(self, user:User, products:list[Product], timestamp:str)
    """
    def __init__(self, user:User, products:list[Product], timestamp:str):
        self.user = user
        self.products = products
        self.timestamp = timestamp
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Root: user = {self.user.__str__()}, products = {[x.__str__() for x in self.products]}, timestamp = {self.timestamp.__str__()}'
    def __repr__(self):
        return f'Root(user={repr(self.user)}, products={repr(self.products)}, timestamp={repr(self.timestamp)})'
    def to_dict(self)->dict:
        return {"user": self.user.to_dict(), "products": [x.to_dict() for x in self.products], "timestamp": self.timestamp}
    @classmethod
    def from_dict(cls, data:dict)->'Root':
        if "user" in data and "products" in data and "timestamp" in data:
            classlist_products = [Product.from_dict(classdata) for classdata in data.get("products", [])]
            return cls(User.from_dict(data["user"]), classlist_products, data["timestamp"])
        else:
            raise KeyError("Invalid data for Root")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Root':
        if seed:
            random.seed(seed)
        user = User.from_random(seed, lowlim, uplim)
        products = [Product.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        timestamp = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(user, products, timestamp)
