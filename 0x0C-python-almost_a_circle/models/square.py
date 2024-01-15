#!/usr/bin/python3
"""Square Model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the square"""
        for idx, value in enumerate(args):
            if idx == 0:
                self.id = value
            if idx == 1:
                self.size = value
            if idx == 2:
                self.x = value
            if idx == 3:
                self.y = value
        if not args and len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Dictionary representaion of Square class"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }

    def __str__(self):
        """String representaion for square class"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
