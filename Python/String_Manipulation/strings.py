#***********String slicing*******
# greeting = "Hello,!"
# name = "John Smith"

# X = greeting + " " + name[0:4]
# print(X)

#*********Concatenation*******
# greeting = "Hello "
# name = "Jane Doe"

# Y = greeting + name
# print(Y)

# print(help(str))


#*********String methods*******
# name = "john smith"
# newname = "John"


#1. capitalize METHOD
# name = "john smith"
# cap_name = name.capitalize()
# print(cap_name)

#2. ****Upper() METHOD***
# upper_name = "john smith"
# cap_name = upper_name.upper()
# print(cap_name)

#3. ****Lower() METHOD***
# lower_name = "JOHN SMITH"
# cap_name = lower_name.lower()
# print(cap_name)

#4. ****Count() METHOD***
# print(name.count('o'))
# phone = "0726-123-456"
# phone_new = ["0726" "123" "456"]

#5.****split() METHOD***
# new_list = name.split()
# print(new_list)
# new_phone = phone.split()
# print(new_phone)

# new_phone = phone.split('-')
# print(new_phone)

#*****Not part of this topic******
# my_name = "Abednego Kipngeno Bett"
# new_li = my_name.split()
# middle_name = new_li[1]
# print(middle_name)

#6.********Join()method********
# new_list = phone.split()
# print(new_list)
# phone = "-".join(new_list)
# print(phone)
# joined_phnone = ''.join(phone_new)
# print(joined_phnone)

# print(type(phone))
# print(type(joined_phnone))

#7.*****isalnum method******(alphanumeric method)
# python3 = "python3"
# print(python3.isalnum())

#8.*****isalpha method******(alphabetic method)
# python = "python"
# print(python.isalpha())

#9.*****isdigit method******(digit method)
# text = "python123"
# text2 = "123445"
# print(text.isdigit())
# print(text2.isdigit())

#10.*****isspace method******(space method)
# text = "python"
# text2 = " -"
# print(text.isspace())
# print(text2.isspace())

#11.*****startswith method******
# text = "python"
# print(text.startswith('p'))

#12.*****endswith()   method******
# text = "python"
# print(text.endswith('n'))

#13.*****replace()   method******
# text = "python"
# print(text.replace('p', 'P'))
# text = "i love python"
# print(text.replace('python', 'Javascript'))

#14.*****find() method******
# text = "python"
# print(text.find('t'))

#*****strip() method******
# text = "  python"
# text2 = text.strip()
# print(text)
# print(text2)


#15.****f-string******

#old way of formatiing string
# string = "John"
# age = 30
# height = 5.6
# print("Hello, {} you are {} years old and {} tall".format(string, age, height))

# latest way of f-string
# print(f"Hello, {string} you are {age} years old and {height} tall")
# print(f"Hello, {string} you are {age+5} years old and {height +0.5} tall")
# print(f"Hello, {string.upper()} you are {age+5} years old and {height +0.5} tall".upper()) #capitalization
# print(f"Hello, {string.upper()} you are {age+5} years old and {height +0.5} tall") #capitalization of only sinler strings

print("Hello Rop, How can ia assist you?\n" + "Do you need some python concepts?\n" + "Please lemme know about them")




