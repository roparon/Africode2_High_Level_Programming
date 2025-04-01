# students = {
#     "name": "John Doe",
#     "age": 20,
#     "is_student": True,
#     "courses": ["Math", "Science", "History"],
#     "graduation_year": 2025,
#     "GPA": 3.8,
# }
# Atributes - properties of an object
# Methods - functions that belong to an object
# Class - a blueprint for creating objects
# Object - an instance of a class

# human = {
#     "tribe": "Kalenjin",
#     "age": 85,
#     "is_alive": True,
#     "hobbies": ["running", "reading", "writing"],
#     "married": False,
#     "children": 5,
#     "height": 1.75,
#     "weight": 70,
#     "eye_color": "brown",
#     "hair_color": "black",
#     "blood_type": "O+",
# }

#class - A blueprint for creating objects.
# It defines the properties and methods that the objects will have.
# The __init__ method is a special method that is called when an object is created.
# It initializes the object's properties.



class Student:
    def __init__(self, name, age, id_number = None, courses = None):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.courses = courses if courses is not None else []
enock = Student("Enock", 20, id_number = "12345", courses = ["Python"])
rop = Student("Rop", 20, id_number = "12345", courses =["Java", "Javascript"])
print(f"Student_name is{enock.name} and age is {enock.age} courses:{enock.courses}")
print(f"Student_name is{rop.name} and age is {rop.age}")
