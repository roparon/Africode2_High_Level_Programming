class Students:

    def enroll(self):
        pass

    def gratuate(self):
        pass


class Graduates(Students):
    def __init__(self):
        super().__init__()
    def enroll(self):
        return "Graduates enrolled."

    def gratuate(self):
        return "Graduates graduated."

vague_students = Students()

#print(vague_students.enroll)