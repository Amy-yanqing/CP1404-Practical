"""Band class."""


class Band:
    """Band class."""

    def __init__(self, name):
        """Construct a Band with a name and list of musicians"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.name} ({','.join([str(musician) for musician in self.musicians])}"

    def add(self, musician):
        """Add a musician to a band."""
        self.musicians.append(musician)

    def play(self):
        """Return strings about musician playing their instrument"""
        return '\n'.join([musician.play() for musician in self.musicians])

