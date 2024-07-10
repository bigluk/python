# Python

The following is a brief summary of the Python basic concepts.

## Index

	1. Data Types
	
	2. Numbers
	Definition, Arithmetic Operators
	
	3. String
	Definition, Quotes inside Quotes, Strings are Arrays, String method
	
	4. Variable
	
	5. Data Structure
	list, set, tuple, dictionary

	5. Conditional Logic
	if, ternary operator, truthy vs falsey, is vs ==

	6. Looping
	for, while, range(), enumerate(), break,continue,pass

	7. Functions
	definition, arguments, default parameters, *args and **kwargs, walrus operator, DocString
	
	8. Variable Scope
	global keyword, nonlocal keyword
	
	9. OOP in Python
	class, init method, private vs public, @classmethod and @staticmethod, inheritance, polymorphism, dunder methods
	
	10. Functional Programming
	pure functions, map(), filter(), zip(), reduce(), lambda expression
	
	11. Decorators
	definition, example and usage
	
	12 Error Handling
	try except, many Exceptions, finally, raise
	
	13. Generators
	definition, yield, use case, generator comprehension, generators performance
	
	14. File I/O
	open(), read(), cursor, write() and append(), create a new file, close file

	15. Regular Expression
		 
	


## Data Types
Python has the following data types built-in by default, in these categories:

	1. Text Type:	
     str
	2. Numeric Types:
     int, float, complex
	3. Boolean Type:
     bool
	4. Binary Types:
     bytes, bytearray, memoryview
	5. None Type:
     NoneType, it is a special "type" that represent nothing. When we see a variable set to None
     we know that the variable have no data type.

 
  **_NOTE:_** To discover what kind of data type a variable is we can use the type() function.


## Numbers
### Definition
In python there 3 numbers data types:

	* __int__
	that represent all the integer number
	
	* __float__
	that represent all the floating number
	
	* __complex__
	that represent the boolean value 0 and 1
	
	
Example:

	x = 1    # int
	y = 2.8  # float
	z = 1j   # complex
	
		
### Arithmetic Operators

There are 7 arithmetic operators in Python to work with Numbers data types:

	__Addition Operator +__  
	Addition: adds two operands	x + y

	__Subtraction Operator –__
	Subtraction: subtracts two operands	x – y

	__Multiplication Operator *__ 
	Multiplication: multiplies two operands	x * y

	__Division Operator /__ 
	Division (float): divides the first operand by the second	x / y

	__Floor Division Operator //__ 
	Division (floor): divides the first operand by the second x // y

	__Modulus Operator %__ 
	Modulus: returns the remainder when the first operand is divided by the second	x % y

	__Exponentiation Operator **__ 
	Power (Exponent): Returns first raised to power second	x ** y
	




## String
### Definition
In Python, strings are used for representing textual data. A string is a sequence of characters enclosed in either single quotes ('') or double quotes ("").

### Quotes inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
	
	"It's alright"
	"He is called 'Johnny'"
	'He is called "Johnny"'
	
	
### Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.


###Python String Methods
Python has a set of built-in methods that you can use on strings.

**_NOTE:_** 
All string methods returns new values. They do not change the original string.

	capitalize()	Converts the first character to upper case
	casefold()	Converts string into lower case
	count()	Returns the number of times a specified value occurs in a string
	endswith()	Returns true if the string ends with the specified value
	find()	Searches the string for a specified value and returns the position of where it was found
	index()	Searches the string for a specified value and returns the position of where it was found
	isalnum()	Returns True if all characters in the string are alphanumeric
	isalpha()	Returns True if all characters in the string are in the alphabet
	isdigit()	Returns True if all characters in the string are digits
	islower()	Returns True if all characters in the string are lower case
	isnumeric()	Returns True if all characters in the string are numeric
	join()	Converts the elements of an iterable into a string
	lower()	Converts a string into lower case
	replace()	Returns a string where a specified value is replaced with a specified value
	rsplit()	Splits the string at the specified separator, and returns a list
	startswith()	Returns true if the string starts with the specified value
	strip()	Returns a trimmed version of the string



	
## Variable
A variable, such as in all the other programming language, is an abstract storage location paired with an associated symbolic name, 
which contains some known or unknown quantity of data or object referred to as a value.

In pyhton the variables name follow these rules:
	
	* A variable name must start with a letter or the underscore character
	* A variable name cannot start with a number
	* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
	* Variable names are case-sensitive (age, Age and AGE are three different variables)
	* A variable name cannot be any of the Python keywords.

**_NOTE:_** 
Best practice for naming a variable is that it should be lowercase, with words separated by underscores as necessary to improve readability.



## Data Structure
There are 4 maintypes in Python used to store collections of data: List, Tuple, Set, Dictionary, all with different qualities and usage.
Let's start with vocabulary:

	1. Ordered
	When we say that a data structure are ordered, it means that the items have a defined order, and that order will not change.
	If you add new items to a list, the new items will be placed at the end of the list.
	
	2. Changeable
	When we say that a data structure is changeable, it means that we can change, add, and remove items in a list after it has been created.
	
	3. Allow Duplicates
	When we say that a data structure is indexed, it means that it can have items with the same value.

Now we have the basic vocabulary to describe the main characteristics of the data structure we can dive deeper into the description of each of them saying that:

	1. __List__ 
	it is a collection which is ordered and changeable. Allows duplicate members.
	__Example:__
		thislist = ["apple", "banana", "cherry"]
	__Use Case__:
			When you need something that can change its dimension over time. (Like java LinkedList)
	
	2. __Tuple__ 
	it is a collection which is ordered and unchangeable. Allows duplicate members.
	Example:
		mytuple = ("apple", "banana", "cherry")
	__Use Case__:
			When you need something that cannot change its dimension over time. (Like java Array)
	
	3. __Set__ 
	it is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
	Example:
		myset = {"apple", "banana", "cherry"}
	__Use Case__:
			When you need something that cannot change its dimension over time and does not allow duplicate values. (Like java Set)


	
	4. __Dictionary__ 
	it is a collection which is ordered** and changeable. No duplicate members.
	Example:
		thisdict = {
				"brand": "Ford",
				"model": "Mustang",
				"year": 1964
				}
	__Use Case__:
			When you need something that have to be stored as key value. (Like java Map)

	

	
**_NOTE:_** 
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**_NOTE:_** 
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


## Conditional Logic
An "if statement" is written by using the if keyword.

	a = 33
	b = 200
	if b > a:
		print("b is greater than a")
		
**_NOTE:_** 
Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.


### Elif and Else
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
The else keyword catches anything which isn't caught by the preceding conditions.

	a = 200
	b = 33
	if b > a:
		print("b is greater than a")
	elif a == b:
		print("a and b are equal")
	else:
		print("a is greater than b")
		
		
### Ternary operator
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

	a = 2
	b = 330
	print("A") if a > b else print("B")
	
	
### Truthy and Falsy
In Python, individual values can evaluate as either True or False. Values that evaluate to True are "Truthy", and values that evaluate to False are "Falsy".
By default, an object is considered Truthy, unless its __bool__() method returns False or __len__() returns 0.

Example:

	empty_list = []
	empty_touple = ()
	empty_dict = {}
	empty_set = set()
	empty_string = ""
	empty_range = range(0)

	print(bool(empty_list)) # False

	print(bool(empty_touple)) # False

	print(bool(empty_dict)) # False

	print(bool(empty_set)) # False

	print(bool(empty_string)) # False

	print(bool(empty_range)) # False

	print(bool(0)) # False

	print(bool(0.0)) # False

	print(bool(0j)) # False

	print(bool(None)) # False

	print((bool(1))) # True

	print((bool(" "))) # True
	

### is vs ==
The == operator compares the value or equality of two objects, whereas the Python is operator checks 
whether two variables point to the same object in memory.

The == operator relies on the __eq__ object method that specifies how two objects must be compared to understand if they are equal or not.
While the is operator relies on just the position memory of the object, if two object are in the same memory position it means that they are the same object 
and so equal.


## Looping
Python has two primitive loop commands:

	1. for loops
	2. while loops


### for
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
		print(x)
	

### while
With the while loop we can execute a set of statements as long as a condition is true.
	i = 1
	while i < 6:
		print(i)
		i += 1

### range() and enumerate()
In Python, range and enumerate are both built-in functions that are used in different contexts.
The range function is used to generate a sequence of numbers. It can be used in a for loop to iterate a specific number of 
times or to create a list of numbers within a specified range.
The enumerate function, on the other hand, is used to iterate over a sequence (such as a list, tuple, or string) while 
keeping track of the index of each item. It returns pairs of index and value for each item in the sequence.
Here's a simple example to illustrate the difference:

	# Using range
	for i in range(5):
	# This will print numbers from 0 to 4
		print(i)   
 
	# Using enumerate 
	my_list = ['apple', 'banana', 'orange'] 
	for index, value in enumerate(my_list): 
	# This will print pairs of index and value for each item in the list
		print(index, value)   
		

### break, continue and pass
In Python, "break", "continue", and "pass"  are control flow statements used within loops and conditional statements. 

	* "break" is used to exit a loop prematurely if a certain condition is met. It terminates the loop entirely and continues with the next statement after the loop.

	* "continue" is used to skip the rest of the current iteration of a loop and continue with the next iteration. 
	It effectively jumps to the next iteration without executing the remaining code in the loop's body. 
	
	* "pass" is a null operation; it doesn't do anything. It's used as a placeholder when a statement is 
	syntactically required but no action is needed.
	
	
## Function
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
In Python a function is defined using the __def__ keyword:

Function example:
	def my_function():
		print("Hello from a function")

To call a function, use the function name followed by parenthesis:

Example:
	def my_function():
		print("Hello from a function")

	my_function()


### Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, we pass along a first name, 
which is used inside the function to print the full name.

Example:
	def my_function(fname):
		print(fname + " Refsnes")

	my_function("Emil")
	my_function("Tobias")
	my_function("Linus")


### Default Parameters 
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value.

Example:
	def my_function(country = "Norway"):
		print("I am from " + country)

	my_function("Sweden")
	my_function("India")
	my_function()
	my_function("Brazil")


### *args and **kwargs 
In Python, the single-asterisk form of *args can be used as a parameter to send a non-keyworded variable-length argument list to functions. 
It is worth noting that the asterisk (*) is the important element here, as the word args is the established conventional idiom, 
though it is not enforced by the language.
Let’s look at a typical function that uses two arguments:

	def multiply(x, y):
		print (x * y)

In the code above, we built the function with x and y as arguments, and then when we call the function, we need to use numbers to 
correspond with x and y. In this case, we will pass the integer 5 in for x and the integer 4 in for y:

	def multiply(x, y):
		print (x * y)

	multiply(5, 4)

Now, if we run the above code we’ll receive 20 as output, showing that the integers 5 and 4 were multiplied as per the multiply(x,y) function.
What if, later on, we decide that we would like to multiply three numbers rather than just two? 
If we try to add an additional number to the function, as shown below, we’ll receive an error.

	def multiply(x, y):
		print (x * y)

	multiply(5, 4, 3)

Output:

	TypeError: multiply() takes 2 positional arguments but 3 were given
	
So, if you suspect that you may need to use more arguments later on, you can make use of *args as your parameter instead.
We can essentially create the same function and code that we showed in the first example, by removing x and y as function 
parameters, and instead replacing them with *args:

	def multiply(*args):
		z = 1
		for num in args:
			z *= num
		print(z)

	multiply(4, 5)
	multiply(10, 9)
	multiply(2, 3, 4)
	multiply(3, 5, 10, 6)

When we run this code, we’ll receive the product for each of these function calls:

Output: 20, 90, 24, 900

Because we used *args to send a variable-length argument list to our function, we were able to pass in as many arguments 
as we wished into the function calls.
With *args you can create more flexible code that accepts a varied amount of non-keyworded arguments within your function.

Now, let's continue with the double asterisk form of **kwargs. It is used to pass a keyworded, variable-length argument 
dictionary to a function. Again, the two asterisks (**) are the important element here, as the word kwargs is conventionally 
used, though not enforced by the language.

Like *args, **kwargs can take however many arguments you would like to supply to it. However, **kwargs differs from *args 
in that you will need to assign keywords.

First, let’s print out the **kwargs arguments that we pass to a function. We’ll create a short function to do this:

	def print_kwargs(**kwargs):
        print(kwargs)

Next, we’ll call the function with some keyworded arguments passed into the function:

	def print_kwargs(**kwargs):
        print(kwargs)

	print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)

Let’s run the program above and look at the output:

Output:

	{'kwargs_3': True, 'kwargs_2': 4.5, 'kwargs_1': 'Shark'}

**_NOTE:_** 
Depending on the version of Python 3 you are currently using, the dictionary data type may be unordered. In Python 3.6 and above, 
you’ll receive the key-value pairs in order, but in earlier versions, the pairs will be output in a random order.

What is important to note is that a dictionary called kwargs is created and we can work with it just like we can work with other dictionaries.

Let’s create another short program to show how we can make use of **kwargs. Here we’ll create a function to greet a dictionary of names. 
First, we’ll start with a dictionary of two names:

	def print_values(**kwargs):
		for key, value in kwargs.items():
			print("The value of {} is {}".format(key, value))

	print_values(my_name="Sammy", your_name="Casey")

We can now run the program and look at the output:

Output:

	The value of your_name is Casey
	The value of my_name is Sammy

Again, because dictionaries may be unordered, your output may be with the name Casey first or with the name Sammy first.

Let’s now pass additional arguments to the function to show that **kwargs will accept however many arguments you would like to include:

	def print_values(**kwargs):
		for key, value in kwargs.items():
			print("The value of {} is {}".format(key, value))

	print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )
		
When we run the program at this point, we’ll receive the following output, which may again be unordered:

Output:

	The value of name_2 is Gray
	The value of name_6 is Val
	The value of name_4 is Phoenix
	The value of name_5 is Remy
	The value of name_3 is Harper
	The value of name_1 is Alex

Using **kwargs provides us with flexibility to use keyword arguments in our program. When we use **kwargs as a parameter, 
we don’t need to know how many arguments we would eventually like to pass to a function.


### Walrus Operator
The walrus operator, also known as the assignment expression operator, is a new feature that was introduced in Python 3.8. 
It allows you to assign a value to a variable and use it in the same expression, without having to write it twice. 
The syntax of the walrus operator is :=, and it can be used in places where a regular assignment statement is not allowed, 
such as in a lambda function, a list comprehension, or a conditional expression.
Here is the syntax:

	variable := expression

It got its name from the operator symbol (:=) mimicking the eyes and tusks of a sideways walrus (colon equals operator).
Let's make an example:

	word = "helloooooooo"
	if(len(word) > 10):
		print(f"the word it is not allowed due to its length of: {len(word)}")
	
	word = "helloooooooo"	
	if((length := len(word)) > 10):
		print(f"the word it is not allowed due to its length of: {length}")

In the first case we are forced to use the len() function and recalculate the length while in the second case, using the walrus operator,
we put the length computation in the variable length and use inside the if statment.


### DocString
When it comes to writing clean, well-documented code, Python developers have a secret weapon at their disposal – docstrings. 
Docstrings, short for documentation strings, are vital in conveying the purpose and functionality of Python functions, modules, and classes.
Unlike conventional source code comments, the docstring should describe what the function does, not how.

Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “”” triple double quotes “”” just below the class, method, 
or function declaration. All functions should have a docstring.

Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help function. 
The below examples demonstrate how to declare and access a docstring.

	def divide_numbers(a, b):
		"""
		Divide two numbers.
		
		Parameters
		----------
		a : float
			The dividend.
		b : float
			The divisor.
		
		Returns
		-------
		float
			The quotient of the division.
		"""
		if b == 0:
			raise ValueError("Division by zero is not allowed.")
		return a / b
	print(divide_numbers(3,6))
	
	
## Variable Scope
A variable is only available from inside the region it is created. This is called scope.

### Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

	def myfunc():
		x = 300
		print(x)

	myfunc()
	print(x) // give the error :(NameError: name 'x' is not defined)
	

As explained in the example above, the variable x is not available outside the function, 
but it is available for any function inside the function:
	def myfunc():
		x = 300
		def myinnerfunc():
			print(x)    // this works!
		myinnerfunc()

	myfunc()
	

### Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.

	x = 300

	def myfunc():
		print(x) // this works!

	myfunc()

	print(x) // this works!
	
	
**_NOTE:_** 
If you operate with the same variable name inside and outside of a function, Python will treat them as two 
separate variables, one available in the global scope (outside the function) and one available in the local 
scope (inside the function):

	x = 300
	
	def myfunc():
		x = 200
		print(x)
	
	myfunc()
	
	print(x)

The function will print the local x (200), and then the code will print the global x (300).

### Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.

Example:

	def myfunc():
		global x
		x = 300

	myfunc()

	print(x) // this now works!


Also, use the global keyword if you want to make a change to a global variable inside a function.


	x = 300

	def myfunc():
		global x
		x = 200

	myfunc()
	
	print(x)

The last print(x) will print 200 due to the global keyword inside the myfunc

### Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.
If you use nonlocal, that means that Python will, at the start of the function, look for a 
variable with the same name from one scope above (and beyond).


	def myfunc1():
		x = "Jane"
		def myfunc2():
			nonlocal x
			x = "hello"
		myfunc2()
		return x

	print(myfunc1())
	
The last function prints hello.


## OOP
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.

### Class
A Class is like an object constructor, or a "blueprint" for creating objects.
To create a class, use the keyword class:

	class MyClass:
		x = 5
		
		def mymet():
			pass
		
**_NOTE:_** 
In python the class name follows the camel case convention

**_NOTE:_** 
Class are constituted of attributes (a set of class variables) and method (a set of class function).

### init Method
To create an instance of the class we have to call the constructor:

	p1 =  MyClass()

The constructor is a special method that every class have.
Everytime we want to create a new instance of a specific class we must call this method like we did in the previous example.
Every class has a default constructor but we can create a custom one if we have to define attributes.
To override the default constructor we must specified the init method:

	class Person:
		
		def __init__(self, name, age):
			self.name = name
			self.age = age

	p1 = Person("John", 36)

	print(p1.name)
	print(p1.age)
	
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when 
the object is being created.


### Private vs Public
Control access to methods and attributes is one of the most important aspect in an oop programming language, just think of java!
Python doesn’t have the same notion of private or protected data that Java does. Everything in Python is public. 
Instead of private, Python has a notion of a non-public instance variable. Any variable which starts with an underscore 
character is defined to be non-public. This naming convention makes it harder to access a variable, but it’s only a naming convention, 
and you can still access the variable directly.

	class MyClass:

		x = 5

		def __init__(self, y):
			self.y = y
			self._z = 6

The previous example resume all the above notions. We have a public class variable x, a public class variable to be set in constructor y
and a private class variable to be set in constructor z. 


### @classmethod and @staticmethod


### Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

Any class can be a parent class, so the syntax is the same as creating any other class:

	class Parent:
		
		def __init__(self, fname, lname):
			self.firstname = fname
			self.lastname = lname

		def printname(self):
			print(self.firstname, self.lastname)


To create a class that inherits the functionality from another class, send the parent class as a parameter 
when creating the child class:

	class Child(Parent):
		pass
		
		
Now the Student class has the same properties and methods as the Person class.


**_NOTE:_** 
The super() function is used to give access to methods and properties of a parent or sibling class.
The super() function returns an object that represents the parent class.



### Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
What about classes with child classes with the same name? Can we use polymorphism there?
Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child 
classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

Example
Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

	class Vehicle:
		
		def __init__(self, brand, model):
			self.brand = brand
			self.model = model

		def move(self):
			print("Move!")
	
	
	class Car(Vehicle):
		pass
	
	
	class Boat(Vehicle):
		def move(self):
			print("Sail!")
	
	class Plane(Vehicle):
		def move(self):
			print("Fly!")
	
	car1 = Car("Ford", "Mustang") #Create a Car object
	boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
	plane1 = Plane("Boeing", "747") #Create a Plane object

	for x in (car1, boat1, plane1):
		print(x.brand)
		print(x.model)
		x.move()
		

Child classes inherits the properties and methods from the parent class.
In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
Because of polymorphism we can execute the same method for all classes.


### Multiple Inheritance
Multiple inheritance is a feature in Python that allows a class to inherit attributes and methods from multiple parent classes. 
It provides a mechanism for creating complex class hierarchies and promotes code reuse.
With multiple inheritance, you can combine functionalities from different base classes into a single derived class, resulting 
in more flexible and modular code.
The syntax for implementing multiple inheritance in Python is straightforward. When defining a class, you can specify multiple 
base classes separated by commas.

Here’s an example:

	class DerivedClass(BaseClass1, BaseClass2, ..., BaseClassN):
		# Class definition



### Method Resolution Oredr (MRO)
Method Resolution Order (MRO) is the order in which Python searches for methods in a class hierarchy. When a method is called 
on an object, Python follows a specific order to determine which version of the method to execute. The MRO is calculated 
using the C3 linearization algorithm that is, a depth-first left-to-right ordering. 
This means that when a method is called on an object, it is first searched for in the class of the object. If the method is 
not found there, it is then searched for in the immediate parent class. If there are multiple parent classes, the search proceeds 
from left to right, in the order by which they were declared in the class definition. 
For example, consider a class hierarchy with three classes: A, B, and C. 
Suppose A and B both inherit from C, and printSomething() is called on an object of class C that is not defined in C. 

	class A:
		def printSomething(self):
			print(" In class A")
	
	class B:
		def printSomething(self):
			print(" In class B")
	
	
	# TODO: Inherit class A & B from C
	class C(A, B):
		pass
	
	c = C()
	c.printSomething()
	
       
The method resolution order would be C, A, B. This means that Python would first look for the method in the C class, 
then in the A class (since A is the first parent class listed in the C class definition), and finally in the B class 
(since B is the second parent class listed in the B class definition).

**_NOTE:_** 
if A and B were a child of another class D, the mro wolud have printed C, A, D, B due to the deep first 


### Dunder Methods
Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in 
classes in Python and commonly used for operator overloading. 
They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.

Below are the lists of Python magic methods and their uses.

Initialization and Construction

	__new__: To get called in an object’s instantiation.
	__init__: To get called by the __new__ method.
	__del__: It is the destructor.

Numeric magic methods

	__trunc__(self): Implements behavior for math.trunc()
	__ceil__(self): Implements behavior for math.ceil()
	__floor__(self): Implements behavior for math.floor()
	__round__(self,n): Implements behavior for the built-in round()
	__invert__(self): Implements behavior for inversion using the ~ operator.
	__abs__(self): Implements behavior for the built-in abs()
	__neg__(self): Implements behavior for negation
	__pos__(self): Implements behavior for unary positive 

Arithmetic operators

	__add__(self, other): Implements behavior for math.trunc()
	__sub__(self, other): Implements behavior for math.ceil()
	__mul__(self, other): Implements behavior for math.floor()


String Magic Methods

	__str__(self): Defines behavior for when str() is called on an instance of your class.
	__repr__(self): To get called by built-int repr() method to return a machine readable representation of a type.
	__sizeof__(self): It return the size of the object.

Comparison magic methods

	__eq__(self, other): Defines behavior for the equality operator, ==.
	__ne__(self, other): Defines behavior for the inequality operator, !=.
	__lt__(self, other): Defines behavior for the less-than operator, <.
	__gt__(self, other): Defines behavior for the greater-than operator, >.
	__le__(self, other): Defines behavior for the less-than-or-equal-to operator, <=.
	__ge__(self, other): Defines behavior for the greater-than-or-equal-to operator, >=.
	
	
## Functional Programming
Functional programming (FP) is a declarative software development paradigm that encourages constructing 
programs by composing pure functions and evaluating expressions instead of statements. The functions are 
isolated and independent of the state of the application.
Functional programming is a subset of declarative programming. It also represents a separate programming 
paradigm on its own. In the functional programming approach, developers create programs by composing and 
applying functions.
We can compose function passing a function as argument on another function. We will see this concept in action 
in the next paragraph: map(), filter() etc.
Now, let's explian what is a basic concept of functional programming: the pure functions.

### Pure Functions
Pure functions are functions that always produce the same output for 
the same set of inputs and do not cause any side effects. The application state is not impacted apart from 
the return value of the pure functions and no data is altered. This aspect is known as referential transparency: 
pure functions can be replaced with their returned value without changing the behavior of a program.
That latter property of pure functions can further be defined as immutability. This means that variables or 
objects outside of the function are unaffected. Instead, copies are created and returned from the function if needed.
Generally speaking, FP is about avoiding a shared mutable state, which is when different parts of the program 
are able to access data that can be modified and that exist in a shared scope.

### map()
The map function has the following syntax:

	map(fun, iter)

where:
	* fun: It is a function to which map passes each element of given iterable.
	* iter: It is iterable which is to be mapped.



Example:
 
	def addition(n):
		return n + n
 
	numbers = (1, 2, 3, 4)
	result = map(addition, numbers)
	print(list(result))
	
Result:

	[2, 4, 6, 8]


**_NOTE:_** 
You can pass one or more iterable to the map() function.

	def sumTwoList(x, y):
		return x + y
 
	numbers1 = [1, 2, 3]
	numbers2 = [4, 5, 6]
 
	result = map(sumTwoList, numbers1, numbers2)
	print(list(result))

Result:

	[5, 7, 9]
	
	
	
### filter()
The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

Syntax:

	filter(function, iterable)

Parameters:

	* function	A Function to be run for each item in the iterable
	* iterable	The iterable to be filtered


Example where we want to filter the array, and return a new array with only the values equal to or above 18:

	ages = [5, 12, 17, 18, 24, 32]
	
	def myFunc(x):
		if x < 18:
			return False
		else:
			return True

	adults = filter(myFunc, ages)

	for x in adults:
		print(x)

Result:

	[18, 24, 32]
	

### zip()
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired 
together, and then the second item in each passed iterator are paired together etc.


Syntax:
	
	zip(iterator1, iterator2, iterator3 ...)

Parameters:

	iterable1, iterable2, iterable3 ...	Iterable objects that will be joined together

Example:

	a = ("John", "Charles", "Mike", "Jack")
	b = ("Jenny", "Christy", "Monica", "Vicky")

	x = zip(a, b)

Result:

	(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

	
**_NOTE:_** 
If one tuple contains more items, these items are ignored.

**_NOTE:_** 
If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.


### reduce()
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned 
in the sequence passed along.This function is defined in “functools” module.

How it works:  

	1. At first step, first two elements of sequence are picked and the result is obtained.
	2. Next step is to apply the same function to the previously attained result and the number just succeeding the second 
	   element and the result is again stored.
	3. This process continues till no more elements are left in the container.
	4. The final returned result is returned and printed on console.


Example:
	
	import functools 
  
	lis = [1, 3, 5, 6, 2] 
  
	def sumList(a,b):
		return a+b
  
	print("The sum of the list elements is : ", end="") 
	print(functools.reduce(sumList, lis)) 
  
	def sumListAfterCheck(a,b):
		if a > b:
			return a
		else:
			return b

	print("The maximum element of the list is : ", end="") 
	print(functools.reduce(sumListAfterCheck, lis)) 

Output
The sum of the list elements is : 17
The maximum element of the list is : 6


### Lambda Expression
Python support lambda expression. Lambda expression is a smart and coincisive way to declare a function that we need just in a case.

Syntax:

	lambda arguments : expression
	
Example:

	x = lambda a : a + 10
	print(x(5))

Result:

	15

Use case:
One the most use case is lambda expression with functional paradigm to get more coincisive and clear the code.

 
	numbers = (1, 2, 3, 4)
	result = map(lambda x: x + x, numbers)
	print(list(result))

Output
	[2, 4, 6, 8]

**_NOTE:_** 
Without defining a "classic" function using def we can achieve the same result using the lambda expression.


## Decorators
Python decorators provide an easy yet powerful syntax for modifying and extending the behavior of functions in your code.

### Definition
A decorator in Python is a function that takes another function as an argument and extends its behavior without modifying it. 
The decorator function wraps the original function by defining a wrapper function inside of it. 
This wrapper function executes code before and after calling the original function.
Specifically, when defining a decorator function such as my_decorator in the example, it takes a function as an argument, 
which we generally call func. This func will be the actual function that is decorated under the hood.
The wrapper function inside my_decorator can execute arbitrary code before and after calling func(), which invokes the 
original function. When applying @my_decorator before the definition of my_function, it passes my_function as an argument 
to my_decorator, so func refers to my_function in that context.
The wrapper function then returns the enhanced wrapped function. So now my_function has been decorated by my_decorator. 
When it is later called, the wrapper code inside my_decorator executes before and after my_function runs. This allows 
decorators to transparently extend the behavior of a function, without needing to modify the function itself.
And as you'll recall, the original my_function remains unchanged, keeping decorators non-invasive and flexible.
When my_function() is decorated with @my_decorator, it is automatically enhanced. The my_decorator function here returns a 
wrapper function. This wrapper function gets executed when the my_function() is called now.
First, the wrapper prints "Before the function call" before actually calling the original my_function() function being decorated. 
Then, after my_function() executes, it prints "After function call".
So, additional behavior and printed messages are added before and after the my_function() execution in the wrapper, without 
directly modifying my_function() itself. The decorator allows you to extend my_function() in a transparent way without affecting 
its core logic, as the wrapper handles the enhanced behavior.

### Example and Usage

1. Log Arguments and Return Value of a Function
The Log Arguments and Return Value decorator tracks the input parameters and output of functions. This supports debugging by 
logging a clear record of data flow through complex operations.

	def log_decorator(original_function):
		
		def wrapper(*args, **kwargs):
			print(f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}")

			# Call the original function
			result = original_function(*args, **kwargs)

			# Log the return value
			print(f"{original_function.__name__} returned: {result}")

			# Return the result
			return result
		
		return wrapper

	# Example usage
	@log_decorator
	def calculate_product(x, y):
		return x * y

	# Call the decorated function
	result = calculate_product(10, 20)
	print("Result:", result)
	

Output:

	Calling calculate_product with args: (10, 20), kwargs: {}
	calculate_product returned: 200
	Result: 200

In this example, the decorator function is named log_decorator() and accepts a function, original_function, as its argument. 
Within log_decorator(), a nested function called wrapper() is defined. This wrapper() function is what the decorator returns 
and effectively replaces the original function.
When the wrapper() function is invoked, it prints logging statements pertaining to the function call. Then it calls the 
original function, original_function, captures its result, prints the outcome, and returns the result.
The @log_decorator syntax above the calculate_product() function is a Python convention to apply the log_decorator as a 
decorator to the calculate_product function. So when calculate_product() is invoked, it's actually invoking the wrapper() 
function returned by log_decorator(). Therefore, log_decorator() acts as a wrapper, introducing logging statements before 
and after the execution of the original calculate_product() function.


2. Handle Exceptions and Provide Default Response
The Handle Exceptions decorator is a safety net for functions, gracefully handling exceptions and providing default 
responses when they occur. It shields the application from crashing due to unforeseen circumstances, ensuring smooth operation.


	def handle_exceptions(default_response_msg):
		def exception_handler_decorator(func):
			def decorated_function(*args, **kwargs):
				try:
					# Call the original function
					return func(*args, **kwargs)
				except Exception as error:
					# Handle the exception and provide the default response
					print(f"Exception occurred: {error}")
					return default_response_msg
			return decorated_function
		return exception_handler_decorator

	# Example usage
	@handle_exceptions(default_response_msg="An error occurred!")
	def divide_numbers_safely(dividend, divisor):
		return dividend / divisor

	# Call the decorated function
	result = divide_numbers_safely(7, 0)  # This will raise a ZeroDivisionError
	print("Result:", result)
	Decorator that Handles Exceptions and Provides Default Response


Output:

	Exception occurred: division by zero
	Result: An error occurred!


This code showcases exception handling in functions using decorators.
The handle_exceptions() decorator factory, accepting a default response, produces exception_handler_decorator(). 
This decorator, when applied to functions, attempts to execute the original function. If an exception arises, 
it prints error details, and returns the specified default response.
The @handle_exceptions() syntax above a function incorporates this exception-handling logic. For instance, in 
divide_numbers_safely(), division by zero triggers an exception, which the decorator catches, preventing a crash 
and returning the default "An error occurred!" response.
Essentially, these decorators adeptly capture exceptions in functions, providing a seamless means of incorporating 
handling logic and preventing crashes.



3. Get the Execution Time of a Function
This decorator is your ally in the quest for performance optimization. By measuring and logging the execution time 
of a function, this decorator facilitates a deep dive into the efficiency of your code, helping you pinpoint bottlenecks 
and streamline your application's performance.
It's ideal for scenarios where speed is crucial, such as real-time applications or large-scale data processing. 
And it allows you to identify and address performance bottlenecks systematically.

	import time

	def measure_execution_time(func):
		def timed_execution(*args, **kwargs):
			start_timestamp = time.time()
			result = func(*args, **kwargs)
			end_timestamp = time.time()
			execution_duration = end_timestamp - start_timestamp
			print(f"Function {func.__name__} took {execution_duration:.2f} seconds to execute")
			return result
		return timed_execution

	# Example usage
	@measure_execution_time
	def multiply_numbers(numbers):
		product = 1
		for num in numbers:
			product *= num
		return product

	# Call the decorated function
	result = multiply_numbers([i for i in range(1, 10)])
	print(f"Result: {result}")
	Decorator that displays the execution time of the function


Output:

	Function multiply_numbers took 0.00 seconds to execute
	Result: 362880

This code showcases a decorator that's designed to measure the execution duration of functions.
The measure_execution_time() decorator takes a function, func, and defines an inner function, timed_execution(), 
to wrap the original function. Upon invocation, timed_execution() records the start time, calls the original function, 
records the end time, calculates the duration, and prints it.
The @measure_execution_time syntax applies this decorator to functions below it, such as multiply_numbers(). 
Consequently, when multiply_numbers() is called, it invokes the timed_execution() wrapper, which logs the 
duration alongside the function result.
This example illustrates how decorators seamlessly augment existing functions with additional functionality, 
like timing, without direct modification.


## Error Handling
Python has an error management policy really similar to java.
We have 3 keywords for error handling to remeber:

	1. The try block lets you test a block of code for errors.
	2. The except block lets you handle the error.
	3. The finally block lets you execute code, regardless of the result of the try and except blocks.


### Try except
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement.
The try block will generate an exception, because x is not defined:

	try:
		print(x)
	except:
		print("An exception occurred")

Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error:

	Traceback (most recent call last):
	File "demo_try_except_error.py", line 3, in <module>
	print(x)
	NameError: name 'x' is not defined
	

### Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code 
for a special kind of error:
The following example will print one message if the try block raises a NameError and another for other errors:

	try:
		print(x)
	except NameError:
		print("Variable x is not defined")
	except:
		print("Something else went wrong")
		

### Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.
This can be useful to close objects and clean up resources. The program can continue, without leaving the file object open.
The following example will try to open and write to a file that is not writable:

	try:
		f = open("demofile.txt")
		try:
			f.write("Lorum Ipsum")
		except:
			print("Something went wrong when writing to the file")
		finally:
			f.close()
	except:
		print("Something went wrong when opening the file")
		
		
### Raise
In Python you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.

In the following example we will raise an error and stop the program if x is lower than 0:

	x = -1
	
	if x < 0:
		raise Exception("Sorry, no numbers below zero")
	

The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.

In the following example we will raise a specific error with custome message if x is not an integer:

	x = "hello"
	
	if not type(x) is int:
		raise TypeError("Only integers are allowed")
	

## Generators
Have you ever had to work with a dataset so large that it overwhelmed your machine’s memory? 
Or maybe you have a complex function that needs to maintain an internal state every time it’s called, 
but the function is too small to justify creating its own class. In these cases and more, generators 
and the Python yield statement are here to help.

### Definition
Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. 
These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not 
store their contents in memory.
Generator functions look and act just like regular functions, but with one defining characteristic. 
Generator functions use the Python yield keyword instead of return.

Let's start with an example:

	def infinite_sequence():
		num = 0
		while True:
			yield num
			num += 1

This looks like a typical function definition, except for the Python yield statement and the code that follows it. 
yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.
Instead, the state of the function is remembered. That way, when next() is called on a generator object 
(either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, 
and then yielded again. Since generator functions look like other functions and act very similarly to them, 
you can assume that generator expressions are very similar to other comprehensions available in Python.


### Yield
On the whole, yield is a fairly simple statement. Its primary job is to control the flow of a generator function 
in a way that’s similar to return statements. As briefly mentioned above, though, the Python yield statement has a 
few tricks up its sleeve.
When you call a generator function or use a generator expression, you return a special iterator called a generator. 
You can assign this generator to a variable in order to use it. When you call special methods on the generator, 
such as next(), the code within the function is executed up to yield.
When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. 
(In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved. 
This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.
This allows you to resume function execution whenever you call one of the generator’s methods. 
In this way, all function evaluation picks back up right after yield. 
You can see this in action by using multiple Python yield statements:

	>>> def multi_yield():
	...     yield_str = "This will print the first string"
	...     yield yield_str
	...     yield_str = "This will print the second string"
	...     yield yield_str
	...
	>>> multi_obj = multi_yield()
	>>> print(next(multi_obj))
	This will print the first string
	>>> print(next(multi_obj))
	This will print the second string
	>>> print(next(multi_obj))
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	StopIteration

Take a closer look at that last call to next(). You can see that execution has blown up with a traceback. 
This is because generators, like all iterators, can be exhausted. Unless your generator is infinite, you can iterate 
through it one time only. Once all values have been evaluated, iteration will stop and the for loop will exit. 
If you used next(), then instead you’ll get an explicit StopIteration exception.


### Use case
A common use case of generators is to work with data streams or large files, like CSV files. 
These text files separate data into columns by using commas. This format is a common way to share data. 
Now, what if you want to count the number of rows in a CSV file? The code block below shows one way 
of counting those rows:

	csv_gen = csv_reader("some_csv.txt")
	row_count = 0
	
	for row in csv_gen:
		row_count += 1
	
	print(f"Row count is {row_count}")

Looking at this example, you might expect csv_gen to be a list. To populate this list, csv_reader() opens 
a file and loads its contents into csv_gen. Then, the program iterates over the list and increments 
row_count for each row.
This is a reasonable explanation, but would this design still work if the file is very large? What 
if the file is larger than the memory you have available? To answer this question, let’s assume that csv_reader() 
just opens the file and reads it into an array:

	def csv_reader(file_name):
		file = open(file_name)
		result = file.read().split("\n")
		return result

This function opens a given file and uses file.read() along with .split() to add each line as a separate element to a list. 
If you were to use this version of csv_reader() in the row counting code block you saw further up, 
then you’d get the following output:

	Traceback (most recent call last):
		File "ex1_naive.py", line 22, in <module>
		main()
	File "ex1_naive.py", line 13, in main
	csv_gen = csv_reader("file.txt")
	File "ex1_naive.py", line 6, in csv_reader
	result = file.read().split("\n")
	MemoryError

In this case, open() returns a generator object that you can lazily iterate through line by line. 
However, file.read().split() loads everything into memory at once, causing the MemoryError.

Before that happens, you’ll probably notice your computer slow to a crawl. You might even need to kill the program 
with a KeyboardInterrupt. So, how can you handle these huge data files? Take a look at a new definition of csv_reader():

	def csv_reader(file_name):
		for row in open(file_name, "r"):
			yield row

In this version, you open the file, iterate through it, and yield a row. This code should produce the following 
output, with no memory errors:

	Row count is 64186394

What’s happening here? Well, you’ve essentially turned csv_reader() into a generator function. 
This version opens a file, loops through each line, and yields each row, instead of returning it.


### Generator comprehension
You can also define a generator expression (also called a generator comprehension), which has a very similar syntax 
to list comprehensions. In this way, you can use the generator without calling a function:

	csv_gen = (row for row in open(file_name))

This is a more succinct way to create the list csv_gen.
So, resuming what we said until now, we have to remeber that:

	1. Using yield will result in a generator object.
	2. Using return will result in the first line of the file only.
	

### Generators performance
You learned earlier that generators are a great way to optimize memory. 
While an infinite sequence generator is an extreme example of this optimization, 
let’s amp up the number squaring examples you just saw and inspect the size of the resulting objects. 
You can do this with a call to sys.getsizeof():

	>>> import sys
	>>> nums_squared_lc = [i ** 2 for i in range(10000)]
	>>> sys.getsizeof(nums_squared_lc)
	87624
	>>> nums_squared_gc = (i ** 2 for i in range(10000))
	>>> print(sys.getsizeof(nums_squared_gc))
	120

In this case, the list you get from the list comprehension is 87,624 bytes, while the generator object is only 120. 
This means that the list is over 700 times larger than the generator object!

There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory, 
then list comprehensions can be faster to evaluate than the equivalent generator expression. 
To explore this, let’s sum across the results from the two comprehensions above. 
You can generate a readout with cProfile.run():

	>>> import cProfile
	>>> cProfile.run('sum([i * 2 for i in range(10000)])')
		5 function calls in 0.001 seconds
	
		Ordered by: standard name
	
	
	>>> cProfile.run('sum((i * 2 for i in range(10000)))')
		10005 function calls in 0.003 seconds
	
		Ordered by: standard name
	
	
Here, you can see that summing across all values in the list comprehension took about a third of the time 
as summing across the generator. If speed is an issue and memory isn’t, then a list comprehension 
is likely a better tool for the job.

Remember, list comprehensions return full lists, while generator expressions return generators. 
Generators work the same whether they’re built from a function or an expression. 
Using an expression just allows you to define simple generators in a single line, with an assumed yield 
at the end of each inner iteration.


## File I/O
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

### open()
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

	"r" - Read - Default value. Opens a file for reading, error if the file does not exist
	
	"a" - Append - Opens a file for appending, creates the file if it does not exist
	
	"w" - Write - Opens a file for writing, creates the file if it does not exist
	
	"x" - Create - Creates the specified file, returns an error if the file exists
	
	
In addition you can specify if the file should be handled as binary or text mode

	"t" - Text - Default value. Text mode
	
	"b" - Binary - Binary mode (e.g. images)


To open a file for reading it is enough to specify the name of the file:

	f = open("demofile.txt")
	

### read()
Assume we have a file called demofile.txt, located in the same folder as Python.
Inside that file we have the following lines of text:

	Hello! Welcome to demofile.txt
	This file is for testing purposes.
	Good Luck!

To open the file, use the built-in open() function, described above.
The open() function returns a file object, which has a read() method for reading the content of the file:
Let's see an example:

	f = open("demofile.txt", "r")
	print(f.read())

the output will be:

	Hello! Welcome to demofile.txt
	This file is for testing purposes.
	Good Luck!

If the file is located in a different location, you will have to specify the file path, like this:

	f = open("D:\\myfiles\welcome.txt", "r")
	print(f.read())
	

By default the read() method returns the whole text, but you can also specify how many characters you want to return:
For example, let's return the 5 first characters of the file:

	f = open("demofile.txt", "r")
	print(f.read(5))

the output will be:

	Hello

We can also return one line by using the readline() method.
Let's read one line of the file:

	f = open("demofile.txt", "r")
	print(f.readline())

the output will be:

	Hello! Welcome to demofile.txt

By calling readline() two times, you can read the two first lines:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

the output will be:

	Hello! Welcome to demofile.txt
	This file is for testing purposes.

By looping through the lines of the file, you can read the whole file, line by line:

	f = open("demofile.txt", "r")
	for x in f:
		print(x)


### Cursor
When we open a file, python associates a cursor to the file. A file's cursor is used to store the current position of the 
read and write operations in a file.
For instance, whenever we open a file to read from it, the file cursor is always positioned at 0. 
It is gradually incremented as we progress through the content of the file.
Using the read() function we read the content of the file and to do that we have had to move the cursor to the end of file.

So, if we use read() multiple times, like the following example, what will happen?

	f = open("demofile.txt", "r")
	print(f.read())
	print(f.read())

the output will be:

	Hello! Welcome to demofile.txt
	This file is for testing purposes.
	
we print the file's content just one time... this is due to the fact that with open() we can read the content just one time till 
the cursor reaches the end of file. What can we do to read again the file?
we can use the seek() method, this method hive us the ability to move the cursor where we want in the file, for example, if we
want to start reading the file again from the beginning, we have to do something like this:

	f = open("demofile.txt", "r")
	print(f.read())
	f.seek(0)
	print(f.read())

and the output will be:

	Hello! Welcome to demofile.txt
	This file is for testing purposes.
	
	Hello! Welcome to demofile.txt
	This file is for testing purposes.
	

	
### Write and Append
To write to an existing file, you must add a parameter to the open() function:

	"a" - Append - will append to the end of the file
	
	"w" - Write - will overwrite any existing content


Open the file "demofile2.txt" and append content to the file:

	f = open("demofile2.txt", "a")
	f.write("Now the file has more content!")


Open the file "demofile3.txt" and overwrite the content:

	f = open("demofile3.txt", "w")
	f.write("Woops! I have deleted the content!")



### Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

	"x" - Create - will create a file, returns an error if the file exist
	
	"a" - Append - will create a file if the specified file does not exist
	
	"w" - Write - will create a file if the specified file does not exist



### Close Files
It is a good practice to always close the file when you are done with it.

Close the file when you are finish with it:

	f = open("demofile.txt", "r")
	print(f.readline())
	f.close()


### with statment
So let's recap. To work with files in Python, you have to open the file first. So, the open() function does what the name 
implies – it opens a file for you so you can work with the file.
To use the open function, you declare a variable for it first. The open() function takes up to 3 parameters – 
the filename, the mode, and the encoding. You can then specify what you want to do with the file in a print function.

	my_file = open("hello.txt", "r")
	print(my_file.read())

Output : 
	Hello world
	I hope you're doing well today
	This is a text file

That’s not all. The open() function does not close the file, so you also have to close the file with the close() method.
So, a proper way to use the open function looks like this:

	my_file = open("hello.txt", "r")
	print(my_file.read())
	my_file.close()

Output : 
	Hello world
	I hope you're doing well today
	This is a text file

The read mode is the default file mode in Python, so if you don’t specify the mode, the code above still works fine:

	my_file = open("hello.txt")
	print(my_file.read())
	my_file.close()

Output: 

	Hello world
	I hope you're doing well today
	This is a text file

How Does the With Statement Work in Python?
The with statement works with the open() function to open a file.
So, you can re-write the code we used in the open() function example like this:

	with open("hello.txt") as my_file:
		print(my_file.read())

Output:
 
	Hello world
	I hope you're doing well today
	This is a text file

Unlike open() where you have to close the file with the close() method, the with statement closes the file for you without you telling it to.
This is because the with statement calls 2 built-in methods behind the scene – __enter()__ and __exit()__.
The __exit()__ method closes the file when the operation you specify is done.

With the write() method, you also write to the file as I did below:

	with open("hello.txt", "w") as my_file:
		my_file.write("Hello world \n")
		my_file.write("I hope you're doing well today \n")
		my_file.write("This is a text file \n")
		my_file.write("Have a nice time \n")
	
	with open("hello.txt") as my_file:
		print(my_file.read())

Output:
 
	Hello world 
	I hope you're doing well today
	This is a text file
	Have a nice time
	

## Regular Expression
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

### RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.
We can import the re module as following:

	import re

When you have imported the re module, you can start using regular expressions.
The following example shows how we can use the re module to search the string to see 
if it starts with "The" and ends with "Spain":

	import re
	
	txt = "The rain in Spain"
	x = re.search("^The.*Spain$", txt)


### RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:


	findall	-> Returns a list containing all matches
	search	-> Returns a Match object if there is a match anywhere in the string
	split	-> Returns a list where the string has been split at each match
	sub		-> Replaces one or many matches with a string


### Metacharacters
Metacharacters are characters with a special meaning:

	[]	A set of characters	"[a-m]"	
	\	Signals a special sequence (can also be used to escape special characters)	"\d"	
	.	Any character (except newline character)	"he..o"	
	^	Starts with	"^hello"	
	$	Ends with	"planet$"	
	*	Zero or more occurrences	"he.*o"	
	+	One or more occurrences	"he.+o"	
	?	Zero or one occurrences	"he.?o"	
	{}	Exactly the specified number of occurrences	"he.{2}o"	
	|	Either or	"falls|stays"	
	()	Capture and group	 	 


### Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

	\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
	\b	Returns a match where the specified characters are at the beginning or at the end of a word
	\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
	\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"		
	\D	Returns a match where the string DOES NOT contain digits	"\D"	
	\s	Returns a match where the string contains a white space character	"\s"	
	\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
	\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
	\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
	\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	


### Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

	[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
	[a-n]	Returns a match for any lower case character, alphabetically between a and n	
	[^arn]	Returns a match for any character EXCEPT a, r, and n	
	[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
	[0-9]	Returns a match for any digit between 0 and 9	
	[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
	[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
	[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	
 
### re module functions
The findall() function returns a list containing all matches.

Example: print a list of all matches

	import re
	
	txt = "The rain in Spain"
	x = re.findall("ai", txt)
	print(x)

The list contains the matches in the order they are found.
If no matches are found, an empty list is returned.
 

The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned.

Example: search for the first white-space character in the string.

	import re
	
	txt = "The rain in Spain"
	x = re.search("\s", txt)
	print("The first white-space character is located in position:", x.start())

If no matches are found, the value None is returned.

 
The split() function returns a list where the string has been split at each match.

Example: split at each white-space character.

	import re
	
	txt = "The rain in Spain"
	x = re.split("\s", txt)
	print(x)

 
The sub() function replaces the matches with the text of your choice.

Example: replace every white-space character with the number 9.

	import re
	
	txt = "The rain in Spain"
	x = re.sub("\s", "9", txt)
	print(x)

You can control the number of replacements by specifying the count parameter:

Example: replace the first 2 occurrences.

	import re
	
	txt = "The rain in Spain"
	x = re.sub("\s", "9", txt, 2)
	print(x)
 

