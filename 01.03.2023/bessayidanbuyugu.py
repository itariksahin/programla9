#girilen beş sayıdan büyük olanını bulma
a = int(input('a: ')) 
b = int(input('b: ')) 
c = int(input('c: '))
d = int(input('d: '))
e = int(input('e: '))

if (a > b) and (a > c)and (a>d) and (a>e): 
	print(a, "en büyük sayıdır.") 

elif (b > a) and (b > c)and (b>d) and (b>e): 
	print(b, "en büyük sayıdır.") 

elif (c > a) and (c > b)and (c>d) and (c>e): 
	print(c, "en büyük sayıdır.")
	
elif (d > a) and (d > b)and (d>c) and (d>e): 
	print(d, "en büyük sayıdır.")

elif (e > a) and (e > b)and (e>c) and (e>d): 
	print(e, "en büyük sayıdır.")
