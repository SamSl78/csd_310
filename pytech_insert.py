from pymongo import MongoClient

url = "mongodb+srv://admin:<password>@cluster0.yjadqun.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.0",
            "start_date": "January 1, 2022",
            "end_date": "May 5, 2022",
            "courses": [
                {
                    "course_id": "340",
                    "description": "typing",
                    "instructor": "john",
                    "grade": "A"
                },
                {
                    "course_id": "410",
                    "description": "stressed out",
                    "instructor": "lee",
                    "grade": "F"
                }
            ]
        }
    ]

}

 
bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.5",
            "start_date": "January 1, 2022",
            "end_date": "May 5, 2022",
            "courses": [
                {
                    "course_id": "340",
                    "description": "typing",
                    "instructor": "john",
                    "grade": "B"
                },
                {
                    "course_id": "410",
                    "description": "stressed out",
                    "instructor": "lee",
                    "grade": "A"
                }
            ]
        }
    ]
}


frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "4.0",
            "start_date": "January 1, 2022",
            "end_date": "May 5, 2022",
            "courses": [
                {
                    "course_id": "340",
                    "description": "typing",
                    "instructor": "john",
                    "grade": "C"
                },
                {
                    "course_id": "410",
                    "description": "stressed out",
                    "instructor": "lee",
                    "grade": "B-"
                }
            ]
        }
    ]
}

 
students = db.students

 
print("\n  -- INSERT STATEMENTS --")
thorin_student_id = students.insert_one(thorin).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))

bilbo_student_id = students.insert_one(bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

frodo_student_id = students.insert_one(frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")
