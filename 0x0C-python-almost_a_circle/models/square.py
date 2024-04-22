#!/usr/bin/python3
"""
Model to define a square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """creating a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """starting square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute in order"""
        if args:
            action = {
                    count == 0: self.id = arg,
                    count == 1: self.size = arg,
                    count == 2: self.x = arg,
                    count == 3: self.y = arg
                    }
            for condition, action in action.items():
                if condition:
                    action()
                else continue

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
