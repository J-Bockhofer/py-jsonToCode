class L_1_3:
    def __init__(self, street:str, city:str, state:str):
        self.street = street
        self.city = city
        self.state = state
    def to_dict(self)->dict:
        return {"street": self.street, "city": self.city, "state": self.state}
    @classmethod
    def from_dict(cls, data:dict):
        if "street" in data and "city" in data and "state" in data:
            return cls(data["street"], data["city"], data["state"])
        else:
            raise KeyError("Invalid data for L_1_3")
class L_0_0:
    def __init__(self, name:str, age:int, email:str, address:L_1_3, hobbies:list[str], is_active:bool):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.hobbies = hobbies
        self.is_active = is_active
    def to_dict(self)->dict:
        return {"name": self.name, "age": self.age, "email": self.email, "address": self.address.to_dict(), "hobbies": self.hobbies, "is_active": self.is_active}
    @classmethod
    def from_dict(cls, data:dict):
        if "name" in data and "age" in data and "email" in data and "address" in data and "hobbies" in data and "is_active" in data:
            return cls(data["name"], data["age"], data["email"], L_1_3.from_dict(data["address"]), data["hobbies"], data["is_active"])
        else:
            raise KeyError("Invalid data for L_0_0")
class L_0_1_1:
    def __init__(self, id:int, name:str, price:float):
        self.id = id
        self.name = name
        self.price = price
    def to_dict(self)->dict:
        return {"id": self.id, "name": self.name, "price": self.price}
    @classmethod
    def from_dict(cls, data:dict):
        if "id" in data and "name" in data and "price" in data:
            return cls(data["id"], data["name"], data["price"])
        else:
            raise KeyError("Invalid data for L_0_1_1")
class L_0:
    def __init__(self, user:L_0_0, products:list[L_0_1_1], timestamp:str):
        self.user = user
        self.products = products
        self.timestamp = timestamp
    def to_dict(self)->dict:
        return {"user": self.user.to_dict(), "products": [x.to_dict() for x in self.products], "timestamp": self.timestamp}
    @classmethod
    def from_dict(cls, data:dict):
        if "user" in data and "products" in data and "timestamp" in data:
            classlist_products = [L_0_1_1.from_dict(classdata) for classdata in data.get("products", [])]
            return cls(L_0_0.from_dict(data["user"]), classlist_products, data["timestamp"])
        else:
            raise KeyError("Invalid data for L_0")
