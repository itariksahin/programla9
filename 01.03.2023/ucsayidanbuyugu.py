#girilen üç sayıdan büyük olanını bulma
a = int(input('a: ')) 
b = int(input('b: ')) 
c = int(input('c: '))

if (a > b) and (a > c): 
	print(a, ‘’en büyük sayıdır.’’) 

elif (b > a) and (b > c): 
	print(b, ‘’en büyük sayıdır.’’) 

elif (c > a) and (c > b): 
	print(c, ‘’en büyük sayıdır.’’)
