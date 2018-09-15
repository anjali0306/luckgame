import random

def dice1():
   
    var=raw_input("user1 please type yes for playing ")
    var1=var.strip()
    var2=var1.lower()
    if var2=="yes":
        y=random.randint(min,max)
    elif var2=="no":
        exit()
    else:
       check()
    return(y)
 
def dice2():
   
    var3=raw_input("user2 please type yes for playing ")
    var1=var.strip()
    var2=var1.lower()
    if var2=="yes":
        y=random.randint(min,max)
    elif var2=="no":
        exit()
    else:
       check()
    return(y)


def check():
	count1=0
	while True:
		var4=raw_input("Please enter either yes or no!")
		if var4=="yes":
			x=random.randint(min,max)
		elif var4=="no":
			exit()
		else:
			print("you have only "+ str(4-count1) +" atempts left")
			count1=count1+1
			if count1 >4:
				exit()

var=raw_input("do u want to play dice ")
var1=var.strip()
var2=var1.lower()
if var2=="yes":
	min=input("enter minm value ")
	max=input("enter max value ")
elif var2=="no":
	exit()
else:
	check()















