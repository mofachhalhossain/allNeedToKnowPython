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


''' Numeric operators '''

''' addition +
subtraction -
multiplication *
exponentiation **
division / (float)
division // (floor)
modulus % '''


''' Comparison Operators '''
''' greater than >
less than <
equals ==
not equal !=
greater than or equals >=
less than or equals <= '''


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