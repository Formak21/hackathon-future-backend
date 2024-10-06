# import time
#
#
# class User:
#     def __init__(self):
#         self.id = 0
#         self.first_name = ""
#         self.mid_name = ""
#         self.last_name = ""
#         self.tags = []  # list of strings
#         self.email = ""
#         self.role = ""
#         self.info = ""
#         self.hashed_password = ""
#         self.operators = "" # ?
#
#
class Project:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.head = []  # list of Users
        self.orgs = []  # list of Users
        self.experts = []  # list of Users
        self.volonteers = []  # list of Users
        self.short_info = "" #o
        self.goals = ""
        self.contacts = "" #o
        self.requirements = "" #o
        self.tags = []  # list of strings
        self.region = ""
        self.format = "" #o
        self.url_for_preview = "" #o
        self.docs = []
#
#
# class ProjectShort:
#     def __init__(self):
#         self.id = 0
#         self.title = ""
#         self.short_info = ""
#         self.region = ""
#         self.format = ""
#         self.tags = []  # list of string
#         self.url_for_preview = ""
#
#
# class Feed:
#     def __init__(self):  #
#         self.id = 0
#         self.title = ""
#         self.url_for_preview = ""
#         self.tags = []
#         self.format = ""  # [туториал/хак/etc]
#         self.text = ""
#         self.project_id = 0
#
#
# class Comment:
#     def __init__(self):
#         self.id = 0
#         self.Feed_id = 0
#         self.text = ""
#
#
# class Chat:
#     def __init__(self):
#         self.id = 0
#         self.first_user = 0
#         self.second_user = 0
#
#
# class Message:
#     def __init__(self):
#         self.id = 0
#         self.chat_id = 0
#         self.create_time = time.time()
#         self.type = ""
#         self.data = ""
#
#
# class Notification:
#     def __init__(self):
#         self.id = 0
#         self.type = ""
#         self.data = ""
#         self.user_id = 0
#
# class session:
#     def __init__(self):
#         self.session_id = "" # это уже UUID
#         self.user_id=""