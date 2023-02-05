from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.yjadqun.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students

student_list = students.find({})

print("DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

new_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}


new_doc_id = students.insert_one(new_doc).inserted_id


print("INSERT STATEMENTS")
print("  Inserted student record into the students collection with document_id " + str(new_doc_id))


student_new_doc = students.find_one({"student_id": "1010"})


print("DISPLAYING STUDENT NEW DOC")
print("  Student ID: " + student_new_doc["student_id"] + "\n  First Name: " + student_new_doc["first_name"] + "\n  Last Name: " + student_new_doc["last_name"] + "\n")


deleted_student_new_doc = students.delete_one({"student_id": "1010"})


new_student_list = students.find({})

 
print("DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY")


for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


input("End of program, press any key to continue...")
