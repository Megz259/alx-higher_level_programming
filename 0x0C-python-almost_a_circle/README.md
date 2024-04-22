#0x0C. Python - Almost a circle
#Tasks

0. If it's not tested it doesn't work
mandatory
All your files, classes and methods must be unit tested and be PEP 8 validated.

1. Base class
mandatory
Write the first class Base:

2. First Rectangle
mandatory
Write the class Rectangle that inherits from Base:

3. Validate attributes
mandatory
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

4. Area first
mandatory
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

5. Display #0
mandatory
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

6. __str__
mandatory
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

7. Display #1
mandatory
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

8. Update #0
mandatory
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

9. Update #1
mandatory
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

10. And now, the Square!
mandatory
Write the class Square that inherits from Rectangle:

11. Square size
mandatory
Update the class Square by adding the public getter and setter size

12. Square update
mandatory
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

13. Rectangle instance to dictionary representation
mandatory
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:

14. Square instance to dictionary representation
mandatory
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

15. Dictionary to JSON string
mandatory
JSON is one of the standard formats for sharing data representation.

16. JSON string to file
mandatory
Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

17. JSON string to dictionary
mandatory
Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

18. Dictionary to Instance
mandatory
Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:

19. File to instances
mandatory
Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

20. JSON ok, but CSV?
#advanced
Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:

21. Let's draw it
#advanced
Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:


