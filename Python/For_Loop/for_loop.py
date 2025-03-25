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

students = ["Dorothy", "Rop", "Kirui", "Enock", "Kipngeno"]
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



#*****We cannont use the above method in iterating over sets********************************
# set_students = set(students)
# for index in range(len(set_students)):
#     print(index, set_students[index])

#Method3: Using enumerate() function
#enumerate() function is used to add a counter to an iterable and returns it in a form of enumerate object
#The syntax is enumerate(iterable, start)
#iterable: any object that supports iteration
#start: the index value from which the counter should start
#The default value of start is 0
#The enumerate object can be converted to a list, tuple or set
#The enumerate object can be used in a for loop
#The enumerate object can be used to create a dictionary
#The enumerate object can be used to create a list of tuples,lists,strings,sets,dictionaries, integers, floats, booleans, None, variables, functions, classes, objects, modules and classes
#(a) list
# for i, student in enumerate(students):
#     print(i, student)

# for i, student in enumerate(students, start = 1):
#     print(i, student)

#**************PASS***************************
#The pass statement is used to do nothing
#The pass statement can be used as a placeholder
#The pass statement can be used to avoid getting an error e.g: indentation, syntax, runtime, logical, semantic, type,value, name, attribute, key, index errors.
for student in students:
    pass

#**************Else***************************
#The else statement is used to execute a block of code when the loop is finished

for student in students:
    if student == "Kipngeno":
        continue
    print(student)
else:
    print("The list ends here")