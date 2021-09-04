print("Hello World!")


''' backslash characters/escape sequence and comment '''
# single line comment
'''Multiple
    Line
    Comment.'''

print("Hello People!\n Welcome to Python")
''' for tab \t, for print double quote (" \"\" ") '''
print("Name: \"John Smith\", \n Age: \"23\"")


''' variables '''
''' In other programming languages like C, C++, and Java, you will need to declare the
 type of variables but in Python you don’t need to do that. Just type in the variable
  and when values will be given to it, then it will automatically know whether the 
  value given would be an int, float, or char or even a String. '''

name = "Richi Ria";
age = 23;
college = "University of Valencia";
gpa = "69%"
''' age type conversion int to string  '''
print("Name: "+name+" Age: "+str(age)+" College: "+college+" GPA: "+gpa)
''' no type conversion '''
print("Name: "+name+" Age: ",age," College: "+college+" GPA: "+gpa)

''' Namespaces/variable types or local, global, inner variables '''

''' # var1 is in the global namespace
var1 = 5
def some_func():

	# var2 is in the local namespace
	var2 = 6
	def some_inner_func():

		# var3 is in the nested local
		# namespace
		var3 = 7

 '''

"""  Numeric operators  """

''' addition +
	subtraction -
	multiplication *
	exponentiation **
	division / (float)
	division // (floor)
	modulus % 
'''


''' Comparison Operators '''
''' greater than >
	less than <
	equals ==
	not equal !=
	greater than or equals >=
	less than or equals <= 
'''


''' logical operators '''

''' and	-> Logical AND: True if both the operands are true	x and y
or ->	Logical OR: True if either of the operands is true 	x or y
not ->	Logical NOT: True if operand is false 	not x '''

# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)


""" Bitwise Operators """

""" 
&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<< 
"""
print("Bitwise operator: ")
# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)


''' Identity Operators '''

''' (is and is not) are the identity operators both are used to check if two values 
are located on the same part of the memory. Two variables that are equal do not 
imply that they are identical. '''

a = 10
b = 20
c = a

print(a is not b)
print(a is c)


""" Membership Operators

in and not in are the membership operators; used to test whether a value or variable is in a sequence.

in            True if value is found in the sequence
not in        True if value is not found in the sequence

 """

x = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")


''' ternary operator: '''

a, b = 10, 20

min = a if a < b else b
print(min)


""" console input """

val = input("What's your name?")
print("Your name is: ",val)

#type casting
integer = int(input("Enter any digit"))
print("You entered: ", integer)

'''taking multiple input'''
x,y = input("Enter values: ").split()
print("values: ", x,y)

# type casting
a, b = [int(a) for a in input("Enter Integers: ").split()]
print("Integer values: ", a,b)


'''End parameter in print()'''
print("Hello", end=' ')
print("World!", end='\n')

'''Separate parameter in print()'''
print('13','4','1994', sep='-')
print("mr","gmail.com", sep='@')