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
