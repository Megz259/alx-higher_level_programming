#!/usr/bin/python3
"""
Defining a rectangular class
"""


class Rectangle:
    """
    Creating a rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Creating a rectangle

        Args:
        width (int): width of rectangle
        height (int): heisght of rectangle
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """
            getting the width of the rectangle
            """

            return self.__width

        @width.setter
        def width(self, value):
            """
            Args:
            value (int): widths of rectangle

            Attributes:
            __width (int): width of rectangle

            Raise:
            TypeError: if not and int
            ValueError: if less than 0
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
        def height(self):
            """
            getting the height of a rectangle
            """

            return self.__height

        @height.setter
        def height(self, value):
            """
            Args:
            value (int): height of rectangle

            Attributes:
            __height (int): height of rectangle

            Raises:
            TypeError: if not an int
            ValueError: if less than 0
            """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

            def area(self):
                """
                Returns the area of a rectangle
                Attributes:
                    __width: width
                    __height: height

                    Return:
                        Answer
                        """

                return (self.__width * self.__height)

            def perimeter(self):
                """
                Returns the perimeter
                Attributes:
                    __width: width
                    __height: height

                    Return:
                        answer or 0
                        """

                if self.__width is 0 or self.__height is 0:
                    return 0
                else:
                    return((self.__width * 2) + (self.__height * 2))

                def __str__(self):
                    """
                    Prints the rectangle (with the # character)
                    """

                    if self.__width == 0 or self.__height == 0:
                        return ("")

                    rect = []
                    for i in range(self.__height):
                        [rect.append('#') for x in range(self.__width)]
                        if i != self.__height - 1:
                            rect.append("\n")
                            return ("".join(rect))

                        def __repr__(self):
                            """
                            Return the string
                            """
                            rect = "Rectangle(" + str(self.__width)
                            rect += ", " + str(self.__height) + ")"
                            return (rect)

                        def __del__(self):
                            """
                            Create a message for every deletion
                            """
                            print("Bye rectangle...")
