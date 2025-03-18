class Student:
    def __init__(self, name, family_name, year):
        self.name = name
        self.family_name = family_name
        self.year = year

    def _get_courses(self):
        pass


if __name__ == "__main__":
    student = Student("Juan", "Trenado", "2025")
    print(student.name, student.family_name)
