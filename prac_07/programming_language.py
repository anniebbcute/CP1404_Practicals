class ProgrammingLanguage:

    def __init__(self, title, typing, reflection, year):
        self.title = title
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.title, self.typing,
                                                 self.reflection, self.year)
