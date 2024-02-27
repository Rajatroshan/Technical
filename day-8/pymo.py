from pymongo import MongoClient
client =MongoClient()
dbname=client["samp"]
collection_name=dbname['students']

class personal:

    def __init__(self):
        self.college_name="GIETU"
        self.year=2024

class student(personal):

    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
        self.personal=vars(personal())

s1=student("John Doe","CSE")
name="John Doe"
dept="CSE"

collection_name.insert_one(vars(s1))
