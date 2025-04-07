while True:
    try:
        user_input = input("Please enter a number: ")
        if user_input == "":
            raise Exception("Input cannot be empty")
        x = int(user_input) 
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except Exception as e:
        print(e)