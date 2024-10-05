class User:
    def __init__(self):
        self.id = 0
        self.first_name = ""
        self.last_name = ""
        self.tags = [] # list of strings
        self.email = ""
        self.role = ""
        self.info = ""

class Project:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.head = [] # list of Users
        self.orgs = [] # list of Users
        self.experts = [] # list of Users
        self.volonteers = [] # list of Users
        self.short_info = ""
        self.goals = ""
        self.contacts = ""
        self.requirements = ""
        self.tags = [] # list of strings
        self.region = ""
        self.format = ""
        self.url_for_preview = ""
