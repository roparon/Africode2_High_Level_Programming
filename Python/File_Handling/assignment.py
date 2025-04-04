#Create afile and implement atleast three methods


New_f = open('assignmentffile.txt', 'r')
# print(New_f.read())
# print(New_f.readline())
# print(New_f.readlines())
# print(New_f.readlines(2))
# print(New_f.reconfigure(encoding='utf-8'))
# print(New_f.fileno())
# New_f.close()

"""trancate - used to resize a file to a specified size."""
New_f = open('assignmentffile.txt', 'r+')
New_f.truncate(11)
New_f.close()

"""seek() - This mode moves the pointer to a specific position"""
New_f = open('assignmentffile.txt', 'r')
New_f.seek(0)
print(New_f.read())
# New_f.close()


""" tell() - return the current position of the pointer"""
New_f = open('assignmentffile.txt', 'r')
print(New_f.tell())
New_f.close()


"""This is combining multiple methods"""
New_f = open('assignmentffile.txt', 'r+')
print(New_f.readline())
New_f.seek(0)
New_f.write("Overwriting the first line\n")
New_f.flush()
New_f.close()

with open('assignmentffile.txt', 'a') as f:
    f.write("This is a new appended line.\n")

# with open('assignmentffile.txt', 'r') as f:
#     print(f.read())

"""this is video copying"""
with open("RandomVideo.mp4", "rb") as b:
    for data in b:
        with open("Iscopied.mp4", "wb") as f:
            f.write(data)