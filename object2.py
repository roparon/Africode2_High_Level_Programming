#Method - Function that belongs to an object (define inside a class)
class Student:
    def __init__(self, name, age, scores, id_number = None, courses = None):
        self.name = name
        self.age = age
        self.scores = scores
        self.id_number = id_number
        self.courses = courses if courses is not None else []
    def pass_fail(self, passing_score=50):
        return "Pass" if self.scores >= passing_score else "Fail"
    def is_active(self):
        if self.courses == []:
            return "Not Enrolled"
        else:
            return "Enrolled"
dorothy = Student("Dorothy", 20, 53, "AASE09")
johnson = Student("Johnson", 23, 46, "AASE03")
print(f"{dorothy.name} of id {dorothy.id_number} has {dorothy.pass_fail()}")
print(f"{johnson.name} of id {johnson.id_number} has {johnson.pass_fail()}")