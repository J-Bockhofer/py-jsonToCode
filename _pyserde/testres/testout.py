class L_3_4_1:
    def __init__(self, type_name:str, alias:str, one_shot:str, capture:str, params:str, suppress:str, info:str):
        self.type_name = type_name
        self.alias = alias
        self.one_shot = one_shot
        self.capture = capture
        self.params = params
        self.suppress = suppress
        self.info = info
    def to_dict(self)->dict:
        return {"type_name": self.type_name, "alias": self.alias, "one_shot": self.one_shot, "capture": self.capture, "params": self.params, "suppress": self.suppress, "info": self.info}
class L_3_5_1:
    def __init__(self, type_name:str, system_base:str, distr:str):
        self.type_name = type_name
        self.system_base = system_base
        self.distr = distr
    def to_dict(self)->dict:
        return {"type_name": self.type_name, "system_base": self.system_base, "distr": self.distr}
class L_2_3_1:
    def __init__(self, type_name:str, alias:str, command:str, info:str, args:list[L_3_4_1], knownHosts:list[L_3_5_1]):
        self.type_name = type_name
        self.alias = alias
        self.command = command
        self.info = info
        self.args = args
        self.knownHosts = knownHosts
    def to_dict(self)->dict:
        return {"type_name": self.type_name, "alias": self.alias, "command": self.command, "info": self.info, "args": [x.to_dict() for x in self.args], "knownHosts": [x.to_dict() for x in self.knownHosts]}
class L_1_3_1:
    def __init__(self, type_name:str, name:str, info:str, command_collection:list[L_2_3_1]):
        self.type_name = type_name
        self.name = name
        self.info = info
        self.command_collection = command_collection
    def to_dict(self)->dict:
        return {"type_name": self.type_name, "name": self.name, "info": self.info, "command_collection": [x.to_dict() for x in self.command_collection]}
class L_0_1_1:
    def __init__(self, type_name:str, name:str, info:str, command_collections:list[L_1_3_1]):
        self.type_name = type_name
        self.name = name
        self.info = info
        self.command_collections = command_collections
    def to_dict(self)->dict:
        return {"type_name": self.type_name, "name": self.name, "info": self.info, "command_collections": [x.to_dict() for x in self.command_collections]}
class L_0:
    def __init__(self, type_name:str, folders:list[L_0_1_1]):
        self.type_name = type_name
        self.folders = folders
    def to_dict(self)->dict:
        return {"type_name": self.type_name, "folders": [x.to_dict() for x in self.folders]}
