"""
Estimate: 30 minutes
Actual: 60 minutes
Programming guitar class
"""
current_year = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar object."""
        return f"{self.name}({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """get age method"""
        return current_year - self.year

    def is_vintage(self):
        """Determine whether a Guitar is considered vintage """
        return self.get_age() >= VINTAGE_AGE
