#write a program that generates 10 random numbers and adds them up
import random

total =0
for i in range (0, 10):

    number= random.randint(0, 100)
    total = total+number

print (total)
