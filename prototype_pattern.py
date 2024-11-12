import copy

# 1. The prototype interface declares the cloning mehthods i.e. clone method
class Shape:
	def clone(self):
		return copy.deepcopy(self)
		# A deep copy constructs a new compound object and then, recursively,
  	# inserts copies into it of the objects found in the original.


# 2. Concrete Prototype Classes: These classes inherit from the prototype interface and implement the cloning method.
class Rectangle(Shape):
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def __str__(self):
		return str(self.height * self.width)
	

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	
	def __str__(self):
		return str(3.14 * self.radius ** 2)

# 3. Client Code: the client can produce a copy of any object that follows the prototype interface.
rectangle = Rectangle(5, 5)
circle = Circle(3)

cloned_rectangle = rectangle.clone()
cloned_circle = circle.clone()

#modification of the cloned instance properties independently of the original
cloned_rectangle.width = 6
cloned_circle.radius = 5

print("Rectangle Area: ", rectangle) #Output: 25
print("Cloned Rectangle Area: ", cloned_rectangle) #Output: 30

print("Circle Area: ", circle) #Output: 28.26
print("Cloned Circle Area: ", cloned_circle) #Output: 78.5
