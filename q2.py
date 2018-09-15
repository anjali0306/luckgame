import os
a=[]
b=[]
n=0

from q1 import dice1,dice2
from q1 import check

def user1(r):
	n=0
	n=n+1
	p=0
	while n<5:
		
		for n in range(r):
			
			if n%2==0:
				p=p+1
				for i in range(p,6):
					a.append(dice1())
					print ( str(i) + " 1st user ")
					break
				user1_sum=sum(a)
				print(sum(a))
			else:
				count=0
				for j in range(p,6):
					b.append(dice2())
					print ( str(j) + " 2nd user")
					break
				user2_sum=sum(b)
				print(sum(b))
	return(user1_sum,user2_sum)	
      	
varReslt=user1(10)
VarReList=list(varReslt)
if VarReList[0]>VarReList[1]:
	print ( "Hurray!! user1 wins ")
	print (VarReList[0],VarReList[1])
else:
	print("Hurray!! user2 wins ")