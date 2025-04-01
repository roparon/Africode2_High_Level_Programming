# Arbitrary args/kwargs
# def course_units(*args):
#     units = []
#     for unit in args:
#         units.append(unit)
#     return units

# course_units("html", "css", "javascript", "python", "django", "flask", True, 102.00, 90)

# def student_info(**infor):
#     student_information = {}
#     for key, value in infor.items():
#         print(f"{key}: {value}")
# print(student_info(name = "Enock", age = 20, course = "html"))

def performance_report(*args, **kwargs):
    print(*args)
    print(kwargs)

performance_report({"Enock": "Kirui", "age" : 20, "score" : 90, "grade" : "A"},)


# def students_info(**info):
#     print(info)
# students_info(name = "Rop", age = 21, course = "Java", status = "active")
def courses(*args):
    print(args)
courses("html", "css", "javascript", "python", "django", "flask")


#change to be a list
def courses(*args):
    courses_list = []
    for course in args:
        courses_list.append(course)
    print(courses_list)

courses("html", "css", "javascript", "python", "django", "flask")
