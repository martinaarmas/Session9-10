
print("Hello")
print("As you can see, each print will start from a new line")
# what if we do not want to end with a new line?
print("we need to use the end argument, ", end="") #end is just the line of text added to the end of the print
print("so we continue on the same line", end="(end can be whatever we want). ")
print("Pretty cool, yes?")
# print can also print expressions
print(2+4)
print("the value of 2+5 is ", 2+5)
print("Python, is 2 greater than 4? the answer is: ", 2 > 4)
print("we can use print as a calculator: ", (2 + 3*2)**2)  # same as (2 + 6) to the power of 2 = 8 x 8 = 64
# we will talk more on how to do math with python
print("we can print a list of items: ", "dog", "cat", "mouse", "elephant", "moose")
print("What if we need to separate the items differently? Let's use the sep argument")
print("we can print a list of items: dog", "cat", "mouse", "elephant", "moose", sep="!!   ",
      end="! just one exclamation for moose\n")
# \n means the newline character, so it instructs the print to start from a newline afterwards
print("This is the end for the", "print", "examples", end=". See you next time!")

