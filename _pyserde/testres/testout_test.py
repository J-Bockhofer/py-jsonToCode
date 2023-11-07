class L_1_4:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
    def to_dict(self)->dict:
        return {"id": self.id, "name": self.name}
    @classmethod
    def from_dict(cls, data:dict):
        if "id" in data and "name" in data:
            return cls(data["id"], data["name"])
        else:
            raise KeyError("Invalid data for L_1_4")
class L_0_1_1:
    def __init__(self, id:int, name:str, department:str, skills:list[str], manager:L_1_4):
        self.id = id
        self.name = name
        self.department = department
        self.skills = skills
        self.manager = manager
    def to_dict(self)->dict:
        return {"id": self.id, "name": self.name, "department": self.department, "skills": self.skills, "manager": self.manager.to_dict()}
    @classmethod
    def from_dict(cls, data:dict):
        if "id" in data and "name" in data and "department" in data and "skills" in data and "manager" in data:
            return cls(data["id"], data["name"], data["department"], data["skills"], L_1_4.from_dict(data["manager"]))
        else:
            raise KeyError("Invalid data for L_0_1_1")
class L_0_2_1:
    def __init__(self, project_id:int, project_name:str, description:str, start_date:str, end_date:str, team:list[int]):
        self.project_id = project_id
        self.project_name = project_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.team = team
    def to_dict(self)->dict:
        return {"project_id": self.project_id, "project_name": self.project_name, "description": self.description, "start_date": self.start_date, "end_date": self.end_date, "team": self.team}
    @classmethod
    def from_dict(cls, data:dict):
        if "project_id" in data and "project_name" in data and "description" in data and "start_date" in data and "end_date" in data and "team" in data:
            return cls(data["project_id"], data["project_name"], data["description"], data["start_date"], data["end_date"], data["team"])
        else:
            raise KeyError("Invalid data for L_0_2_1")
class L_0_3_1:
    def __init__(self, office_name:str, city:str, country:str):
        self.office_name = office_name
        self.city = city
        self.country = country
    def to_dict(self)->dict:
        return {"office_name": self.office_name, "city": self.city, "country": self.country}
    @classmethod
    def from_dict(cls, data:dict):
        if "office_name" in data and "city" in data and "country" in data:
            return cls(data["office_name"], data["city"], data["country"])
        else:
            raise KeyError("Invalid data for L_0_3_1")
class L_0:
    def __init__(self, company:str, employees:list[L_0_1_1], projects:list[L_0_2_1], locations:list[L_0_3_1]):
        self.company = company
        self.employees = employees
        self.projects = projects
        self.locations = locations
    def to_dict(self)->dict:
        return {"company": self.company, "employees": [x.to_dict() for x in self.employees], "projects": [x.to_dict() for x in self.projects], "locations": [x.to_dict() for x in self.locations]}
    @classmethod
    def from_dict(cls, data:dict):
        if "company" in data and "employees" in data and "projects" in data and "locations" in data:
            classlist_employees = [L_0_1_1.from_dict(classdata) for classdata in data.get("employees", [])]
            classlist_projects = [L_0_2_1.from_dict(classdata) for classdata in data.get("projects", [])]
            classlist_locations = [L_0_3_1.from_dict(classdata) for classdata in data.get("locations", [])]
            return cls(data["company"], classlist_employees, classlist_projects, classlist_locations)
        else:
            raise KeyError("Invalid data for L_0")
