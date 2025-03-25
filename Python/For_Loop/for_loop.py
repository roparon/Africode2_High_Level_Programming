# Description: This file is used to demonstrate the for loop in python
#range(start,stop,step)
#start: starting point of the range
#stop: end point of the range
#step: increment value
#If the step value is not provided, then the default value is 1
#If the start value is not provided, then the default value is 0
# for i in range(1,11,2):
#     print(i)

#list

students = ["Dorothy", "Rop", "Kirui", "Enock"]
# for student in students:
#     print(student)
    # print("Hello " + student)
    # print("How are you " + student + "?")
    # print("Welcome to the class " + student)
    # print("*********************")

    #set
# students = set(students)
# print(type(students))
# for student in students:
#     print(student)

#************TASK********************
#Print the student name with the index number
#1 Dorothy
#2 Rop
#3 Kirui
#4 Enock



#adding another variables

# count = 1
# for student in students:
#     print(count, student)
#     count += 1


#Method2 : USing len() and range().

# for count in range(len(students)):
#     print(count, students[count])

    #OR
# for index in range(len(students)):
#     print(count+1, students[index])

set_students = set(students)
for index in range(len(set_students)):
    print(index, set_students[index])