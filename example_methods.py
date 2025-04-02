class Student:
    def __init__(self, name, age, scores, id_number=None, courses=None):
        self.name = name
        self.age = age
        self.scores = scores
        self.id_number = id_number
        self.courses = courses if courses is not None else []

    def pass_fail(self, passing_score=50):
        return "Pass" if self.scores >= passing_score else "Fail"

    def is_active(self):
        return self.age >= 18

    # Method to check if courses list is empty
    def has_courses(self):
        return "No courses" if not self.courses else f"Courses: {self.courses}"

# Example usage
dorothy = Student("Dorothy", 20, 53, "AASE09", [])
johnson = Student("Johnson", 23, 46, "AASE03", ["Math", "Science"])

print(dorothy.has_courses())  # Output: No courses
print(johnson.has_courses())  # Output: Courses: ['Math', 'Science']