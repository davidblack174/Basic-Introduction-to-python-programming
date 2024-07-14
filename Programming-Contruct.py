#Foundation of Programming
#----------------------------------------------
# A program is an instrument giving to the computer to perform a particular task.
# For example 
# x= 2 + 4  <-- An instruction
# x is the identifier in the program
# while 2 + 4 is the Value that the identifier(that is x in this case) is holding in memory  
# The value of x is 6

#----------------------------------------------
# Programming Construct
#----------------------------------------------
# A programming construct is a building block of a program.
# It is a specific way of writing instructions for a program.
# There are three types of programming construct
# 1. Sequence
# 2. Selection
# 3. Iteration
#----------------------------------------------
# Sequence
#----------------------------------------------
# Sequence is the simplest programming construct.
# It is a set of instructions executed in the order they are written.
# For example
# x = 2 + 4
# y = x + 3
# z = x + y
# In the above example, the instructions are executed in the order they are written.
# x is assigned the value of 2 + 4 or x=2+4
# y is assigned the value of x + 3 or y=x+3
# z is assigned the value of x + y or z=x+y
#----------------------------------------------
# Selection
#----------------------------------------------
# Selection is a programming construct that allows the program to decide.
# It is also called decision-making.
# There are two types of selection
# 1. If statement
# 2. Select case statement
#----------------------------------------------
# If Statement
#----------------------------------------------
# The if statement is used to decide based on a condition.
# The condition is a boolean expression evaluated as true or false.
# The statements inside the if block are executed if the condition is true.
# The statements inside the else block are executed if the condition is false.
# For example
# x = 10
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")
# In the above example, the condition x > 5 is true, so the statement "x is greater than 5" is printed. 
#----------------------------------------------
# Select Case Statement
#----------------------------------------------
# The select case statement is used to decide based on multiple conditions.
# It is also called a switch statement in some programming languages.
# For example
# x = 2
# select x:
#     case 1:
#         print("x is 1")
#     case 2:
#         print("x is 2")
#     case 3:
#         print("x is 3")
#     default:
#         print("x is not 1, 2, or 3")
# In the above example, the value of x is 2, so the statement "x is 2" is printed.
# ---------------------------------------------
# NOTE: No Select case in python
#----------------------------------------------
# Iteration
#----------------------------------------------
# Iteration is a programming construct that allows the program to repeat instructions multiple times.
# It is also called looping.
# There are two types of iteration for Python
# 1. For loop or count-controlled loop
# 2. While loop or pre-condition loop
# 3. Do-While loop or post-condition loop (Not available in Python)
#----------------------------------------------
# For Loop or Count-Controlled Loop
#----------------------------------------------
# The for loop is used to iterate over a sequence of elements.
# For example
# for i in range(5):
#     print(i)
# In the above example, the for loop iterates over the range of numbers from 0 to 4 and prints each number.
#----------------------------------------------
# While Loop or Pre-Condition Loop
#----------------------------------------------
# The while loop is used to repeat a set of instructions as long as a condition is true.
# For example
# x = 0 
# while x < 5:
#     print(x)
#     x = x + 1
# In the above example, the while loop repeats the print statement as long as the value of x is less than 5.
# The value of x is incremented by 1 in each iteration.
#----------------------------------------------
# Do-While Loop or Post-Condition Loop
#----------------------------------------------
# The do-while loop is used to repeat a set of instructions at least once and then as long as a condition is true.
# It is not available in Python.

#----------------------------------------------
# Summary
#----------------------------------------------
# Programming constructs are the building blocks of a program.
# They are used to write instructions for a program.
# There are three types of programming constructs:
# 1. Sequence: A set of instructions executed in order.
# 2. Selection: Decision-making based on conditions.
# 3. Iteration: Repeating instructions multiple times.
# Python supports for loop and while loop for iteration.
# Do-while loop is not available in Python.
#----------------------------------------------

