# File input and output.
# This file contains the main function to run the program.
# Open () function (in a file)
# read. write. append
# Close () function


#Syntax
# open("file", "mode")
# open(file, mode)
# file: the name of the file to open
# mode: the mode in which to open the file
# 'r' - read (default)
# 'w' - write - it creates a new file if it does not exist or overwrites the (contents)file if it exists
# 'a' - append - it creates a new file if it does not exist or adds the contents to the end of the file if it exists
# 'r+' - read and write -reads and writes to the file, the file must exist
#  b -binary - reads or writes a file in binary mode

# f = open("test.txt", "r")
# # print(f.read())
# print(f.readline())
# f.close()

#write
# f = open("output.txt", "w")
# # f.write("Hello World")
# f.write("This content will overwrite the previous content")


# # append
# f = open("output.txt", "a")
# f.write("This content will be added to the end of the file")
# f.close()

# # read and write
# f = open("output.txt", "r+")
# print(f.read())
# f.write("This content will be added to the end of the file")
# f.close()


#binary
b = open("image.jpg", "rb")
# print(b.read())

#copy the image
with open("image2.jpg", "rb") as b:
    for data in b:
        with open("copied.jpg", "wb") as f:
            f.write(data)

# with open("filename", "mode") as b:
    #do something with the file
    # pass