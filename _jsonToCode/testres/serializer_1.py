class Address:
    def __init__(self, street:str, city:str, state:str):
        self.street = street
        self.city = city
        self.state = state
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Address: street = {self.street.__str__()}, city = {self.city.__str__()}, state = {self.state.__str__()}'
    def to_dict(self)->dict:
        return {"street": self.street, "city": self.city, "state": self.state}
    @classmethod
    def from_dict(cls, data:dict):
        if "street" in data and "city" in data and "state" in data:
            return cls(data["street"], data["city"], data["state"])
        else:
            raise KeyError("Invalid data for Address")
class User:
    def __init__(self, name:str, age:int, email:str, address:Address, hobbies:list[str], is_active:bool):
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
    def to_dict(self)->dict:
        return {"name": self.name, "age": self.age, "email": self.email, "address": self.address.to_dict(), "hobbies": self.hobbies, "is_active": self.is_active}
    @classmethod
    def from_dict(cls, data:dict):
        if "name" in data and "age" in data and "email" in data and "address" in data and "hobbies" in data and "is_active" in data:
            return cls(data["name"], data["age"], data["email"], Address.from_dict(data["address"]), data["hobbies"], data["is_active"])
        else:
            raise KeyError("Invalid data for User")
class Item:
    def __init__(self, id:int, name:str, price:float):
        self.id = id
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Item: id = {self.id.__str__()}, name = {self.name.__str__()}, price = {self.price.__str__()}'
    def to_dict(self)->dict:
        return {"id": self.id, "name": self.name, "price": self.price}
    @classmethod
    def from_dict(cls, data:dict):
        if "id" in data and "name" in data and "price" in data:
            return cls(data["id"], data["name"], data["price"])
        else:
            raise KeyError("Invalid data for Item")
class Cart:
    def __init__(self, user:User, products:list[Item], timestamp:str):
        self.user = user
        self.products = products
        self.timestamp = timestamp
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'Cart: user = {self.user.__str__()}, products = {[x.__str__() for x in self.products]}, timestamp = {self.timestamp.__str__()}'
    def to_dict(self)->dict:
        return {"user": self.user.to_dict(), "products": [x.to_dict() for x in self.products], "timestamp": self.timestamp}
    @classmethod
    def from_dict(cls, data:dict):
        if "user" in data and "products" in data and "timestamp" in data:
            classlist_products = [Item.from_dict(classdata) for classdata in data.get("products", [])]
            return cls(User.from_dict(data["user"]), classlist_products, data["timestamp"])
        else:
            raise KeyError("Invalid data for Cart")
