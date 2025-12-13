'''name=input("enter your name: ")
age=int(input("enter your age: "))

print(f"Hello, {name}. You're {age} years old!")'''

# --------------------------------------------------------------

def greet(name, age):
    return f"Hello, {name}. You're {age} years old!"

# print(greet('krishna', 24))

# --------------------------------------------------------------

class Person:
	def __init__(self, name, age):
		self.name=name
		self.age=age

	def greet(self):
		return f"Hello {self.name}. You're {self.age} years old!"

#p=Person("Krishna", 24)
#print(p.greet())

# --------------------------------------------------------------

l1=[1,2,3,4,5,"krishna", 4.3, True, False]
print(l1)
