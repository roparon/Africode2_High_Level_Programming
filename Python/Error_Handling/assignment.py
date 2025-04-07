#1. create a custom exception class that inherits from exception
#2. Write a simple try except block and raise that custom exception

# N/B - What you will learn
#     - Custom exception
#     - Raise Exception

# class CustomException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
# try:
#     raise CustomException("This is an exception error.")
# except CustomException as e:
#     print(f"Caught an exception: {e}")


#1. create a custom exception class that inherits from exception

class FileError(Exception):
    def __init__(self, file_name, message):
        super().__init__(message)
        self.file_name = file_name
        self.message = message
#2. Write a simple try except block and raise that custom exception

try:
    file_name = "data.txt"
    raise FileError(file_name, f"Unable to open the file: {file_name}")
except FileError as e:
    print(f"File Error encountered: {e.message} - File: {e.file_name}")
