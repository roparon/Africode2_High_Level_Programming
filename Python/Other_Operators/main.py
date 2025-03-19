# == vs is operators
# == compares the values of the variables
lst1 = ["Enock", "Dorothy", "Kirui", "Rop", "Kipngeno"]
lst2 = ["Enock", "Dorothy", "Kirui", "Rop", "Kipngeno"]
lst3 =lst1
# is compares the memory locations of the variables


# print(lst1 == lst2) # True
# print(lst1 is lst2) # False
# print(lst1 == lst3) # True
# print(lst1 is lst3) # True

x = 10
y = 10
z = 10
# print(id(x))
# print(id(y))
# print(id(z))
# print(x == y) # True
# print(x is y) # True
# print(x == z) # True
# print(x is z) # True
# print(id(lst1))
# print(id(lst2))

# student1 = "Enock"
# student2 = "Enock"
# print(student1 is student1) # True

n = 1000000
m = 1000000
# print(id(n))
# print(id(m))

# in operator
# checks if a value is present in a sequence

# print("Ben" in lst1) # False
# print("Enock" in lst1) # True
# print("Enock" not in lst1) # False

long_string = "Enock is a software developer."
# print("." in long_string) # True
# print("developer" in long_string) # True
# print("Enock is a " not in long_string) # Fals
