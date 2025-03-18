class Course:
    def __init__(self, name, gato):
        self.name = name
        self.gato = gato
        self._post_init()

    def _post_init(self):
        self.semester = self._get_semester()

    def _get_semester(self):
        pass


if __name__ == "__main__":
    course = Course("Algebra")
    print(course.semester)
