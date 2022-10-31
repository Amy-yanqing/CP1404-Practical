"""
Estimate: 30 minutes
Actual: 60 minutes
Programming Language class with tests.
"""


class ProgrammingLanguage:
    def __init__(self, field, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.field},{self.typing} Typing,Reflection={self.reflection},First appeared in {self.year}"


def run_tests():
    """test dynamically language typed """
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.field)


if __name__ == "__main__":
    run_tests()
