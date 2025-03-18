class Degree:
    def __init__(self, name):
        self.name = name
        self._post_init()

    def _post_init(self):
        self.courses = self._get_courses()
        #self.number_of_courses = ""

    def _get_courses(self):
        pass


if __name__ == "__main__":
    degree = Degree("Física")
    print(degree.name)
