students = ["kim", "john", "peter", "jane"]

#1. accessing elements in a list
# print(students[0])
# print(students[3])

#2. modifying elements in a list
#1.append
students.append("sarah")
# 
#2. insert
students.insert(1, "bill")
# 
#3. remove
students.remove("john")
print(students)
#4. pop
students.pop(0)
# print(students)

#5. extend

teachers = ["kimoo", "wilson", "mosses", "rop"]
students.extend(teachers)
# print(students)

#6.concatenation(this is combining list)
africode_community = students + teachers
# print(africode_community)

#8. list indexing
# print(students.index("kimoo"))

#9. list sorting
students.sort()
# print(students)
