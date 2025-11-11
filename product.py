class Product:
    """Product class for storing details of a product."""

    def __init__(self, name="", price=""):
        """Initialises Product object."""
        self.name = name
        self.price = price

    def __str__(self, ):
        """Return a string representation of a Product"""
        return f"{self.name} {self.price}"

    def __repr__(self):
        """Return a developer-friendly string representation of a Guitar."""
        return f"{vars(self)}"
