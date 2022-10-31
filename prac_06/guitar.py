"""
Estimate: 30 minutes
Actual: 60 minutes
Programming guitar class
"""
class Guitar:
    """Represent a Car object.."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar object."""
        return f"{self.name}({self.year}) : ${self.cost:.2f}"


my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(my_guitar)
