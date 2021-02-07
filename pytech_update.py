""" 
    Title: pytech_update.py
    Author: Charles Clark
    Date: February 7, 2021
    Description: Test program for updating a document in the pytech collection
"""

# import
from pymongo import MongoClient

# connection string 
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get students collection 
students = db.students

# find all students in collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and display the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield II"}})

# find the updated student document 
thorin = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# display the updated document
print("  Student ID: " + thorin["student_id"] + "\n  First Name: " + thorin["first_name"] + "\n  Last Name: " + thorin["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
