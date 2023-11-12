import random
import string

class L_1_4:
    """
        L_1_4:
        def __init__(self, id:int, name:str)
    """
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_1_4: id = {self.id.__str__()}, name = {self.name.__str__()}'
    def __repr__(self):
        return f'L_1_4(id={repr(self.id)}, name={repr(self.name)})'
    def to_dict(self)->dict:
        return {"id": self.id, "name": self.name}
    @classmethod
    def from_dict(cls, data:dict)->'L_1_4':
        if "id" in data and "name" in data:
            return cls(data["id"], data["name"])
        else:
            raise KeyError("Invalid data for L_1_4")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_1_4':
        if seed:
            random.seed(seed)
        id = random.randint(lowlim, uplim)
        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(id, name)
class L_0_1_1:
    """
        L_0_1_1:
        def __init__(self, id:int, name:str, department:str, skills:list[str], manager:L_1_4)
    """
    def __init__(self, id:int, name:str, department:str, skills:list[str], manager:L_1_4):
        self.id = id
        self.name = name
        self.department = department
        self.skills = skills
        self.manager = manager
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_1_1: id = {self.id.__str__()}, name = {self.name.__str__()}, department = {self.department.__str__()}, skills = {[x.__str__() for x in self.skills]}, manager = {self.manager.__str__()}'
    def __repr__(self):
        return f'L_0_1_1(id={repr(self.id)}, name={repr(self.name)}, department={repr(self.department)}, skills={repr(self.skills)}, manager={repr(self.manager)})'
    def to_dict(self)->dict:
        return {"id": self.id, "name": self.name, "department": self.department, "skills": self.skills, "manager": self.manager.to_dict()}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_1_1':
        if "id" in data and "name" in data and "department" in data and "skills" in data and "manager" in data:
            return cls(data["id"], data["name"], data["department"], data["skills"], L_1_4.from_dict(data["manager"]))
        else:
            raise KeyError("Invalid data for L_0_1_1")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_1_1':
        if seed:
            random.seed(seed)
        id = random.randint(lowlim, uplim)
        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        department = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        skills = [''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim)) for _ in range(lowlim, uplim)]
        manager = L_1_4.from_random(seed, lowlim, uplim)
        return cls(id, name, department, skills, manager)
class L_0_2_1:
    """
        L_0_2_1:
        def __init__(self, project_id:int, project_name:str, description:str, start_date:str, end_date:str, team:list[int])
    """
    def __init__(self, project_id:int, project_name:str, description:str, start_date:str, end_date:str, team:list[int]):
        self.project_id = project_id
        self.project_name = project_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.team = team
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_2_1: project_id = {self.project_id.__str__()}, project_name = {self.project_name.__str__()}, description = {self.description.__str__()}, start_date = {self.start_date.__str__()}, end_date = {self.end_date.__str__()}, team = {[x.__str__() for x in self.team]}'
    def __repr__(self):
        return f'L_0_2_1(project_id={repr(self.project_id)}, project_name={repr(self.project_name)}, description={repr(self.description)}, start_date={repr(self.start_date)}, end_date={repr(self.end_date)}, team={repr(self.team)})'
    def to_dict(self)->dict:
        return {"project_id": self.project_id, "project_name": self.project_name, "description": self.description, "start_date": self.start_date, "end_date": self.end_date, "team": self.team}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_2_1':
        if "project_id" in data and "project_name" in data and "description" in data and "start_date" in data and "end_date" in data and "team" in data:
            return cls(data["project_id"], data["project_name"], data["description"], data["start_date"], data["end_date"], data["team"])
        else:
            raise KeyError("Invalid data for L_0_2_1")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_2_1':
        if seed:
            random.seed(seed)
        project_id = random.randint(lowlim, uplim)
        project_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        description = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        start_date = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        end_date = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        team = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(project_id, project_name, description, start_date, end_date, team)
class L_0_3_1:
    """
        L_0_3_1:
        def __init__(self, office_name:str, city:str, country:str)
    """
    def __init__(self, office_name:str, city:str, country:str):
        self.office_name = office_name
        self.city = city
        self.country = country
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_3_1: office_name = {self.office_name.__str__()}, city = {self.city.__str__()}, country = {self.country.__str__()}'
    def __repr__(self):
        return f'L_0_3_1(office_name={repr(self.office_name)}, city={repr(self.city)}, country={repr(self.country)})'
    def to_dict(self)->dict:
        return {"office_name": self.office_name, "city": self.city, "country": self.country}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_3_1':
        if "office_name" in data and "city" in data and "country" in data:
            return cls(data["office_name"], data["city"], data["country"])
        else:
            raise KeyError("Invalid data for L_0_3_1")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_3_1':
        if seed:
            random.seed(seed)
        office_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        city = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        country = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(office_name, city, country)
class L_0:
    """
        L_0:
        def __init__(self, company:str, employees:list[L_0_1_1], projects:list[L_0_2_1], locations:list[L_0_3_1])
    """
    def __init__(self, company:str, employees:list[L_0_1_1], projects:list[L_0_2_1], locations:list[L_0_3_1]):
        self.company = company
        self.employees = employees
        self.projects = projects
        self.locations = locations
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0: company = {self.company.__str__()}, employees = {[x.__str__() for x in self.employees]}, projects = {[x.__str__() for x in self.projects]}, locations = {[x.__str__() for x in self.locations]}'
    def __repr__(self):
        return f'L_0(company={repr(self.company)}, employees={repr(self.employees)}, projects={repr(self.projects)}, locations={repr(self.locations)})'
    def to_dict(self)->dict:
        return {"company": self.company, "employees": [x.to_dict() for x in self.employees], "projects": [x.to_dict() for x in self.projects], "locations": [x.to_dict() for x in self.locations]}
    @classmethod
    def from_dict(cls, data:dict)->'L_0':
        if "company" in data and "employees" in data and "projects" in data and "locations" in data:
            classlist_employees = [L_0_1_1.from_dict(classdata) for classdata in data.get("employees", [])]
            classlist_projects = [L_0_2_1.from_dict(classdata) for classdata in data.get("projects", [])]
            classlist_locations = [L_0_3_1.from_dict(classdata) for classdata in data.get("locations", [])]
            return cls(data["company"], classlist_employees, classlist_projects, classlist_locations)
        else:
            raise KeyError("Invalid data for L_0")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0':
        if seed:
            random.seed(seed)
        company = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        employees = [L_0_1_1.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        projects = [L_0_2_1.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        locations = [L_0_3_1.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(company, employees, projects, locations)
