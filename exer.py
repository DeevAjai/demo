#!/bin/python3
"""
l=['apple','banana','cat','mrstvw','bcdy','hklm','dog','mrtk','Hvqn','ALEX','BOSS']

for i in l:
 if {'a','e','i','o','u'} & set(i.lower()):
  pass#rint(i)
 else:
  print(i)
"""
n = int(input())
ans =list()
while n > 1:
	for i in range(9,1,-1):
		while n%i == 0:
			n//=i
			ans.append(i)
	else:
		print("Not");break
for i in ans[::-1]:print(i,end="")
print()
