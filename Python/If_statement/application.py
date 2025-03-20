a = 10
b = 5
c = 10
text = "Hello"
list_x = ["1", "2", "3", "4", "5"]
list_y = ["1", "2", "3", "4", "5"]
list_2 = list_x 

if a > b and c >= a:
    print("a is greater than b and c is greater than or equal to a")
elif a <= b or c != b:
    print("Eithera is less OR equal to b or c is not equal to b")
else:
    print("None of the conditions were met")

if list_x == list_y and list_x is not list_y:
    print("list_x and list_y have the same values but are different objects")
elif not(a==b):
    print("a is not equal to b")
else:
    print("None of the conditions were met")

    if "e" in text and 6 not in list_x:
        print("The letter 'e' is in the text variable and the number 6 is not in the list_x")
    elif "x" not in text and 3 not in list_x:
        print("Either letter 'x' is not in the text variable OR the number 3 is in the list_x")
    else:
        print("None of the membership conditions were met")


if a > b and (3 in list_x or text is not None):
    print("Complex condition met: a is greater than b  AND 3 is in list_x OR text is not None")
elif list_x is list_2 and len(text) > 0:
    print("list_x and list_2 are the same object AND the length of text is greater than 0")
else:
    print("None of the complex conditions were met")