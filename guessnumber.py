import random

x=random.randint(1,100)
print x
y=input("Hey,Please guess the number between 1 and 100 ")
print y
if ( y == x ):
    print("hurray,you guess the right num ")
elif ( y > x ):
    print("hey,ur number guess is greater ")
else:
    print("hey,ur number guess is smaller ")

