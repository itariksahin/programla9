sayac1=1
while(sayac1<11):
    sayac2=0
    if(sayac1%10==0):print("Çarpım taplosu",sayac1,"Lar")
    else:print("Çarpım taplosu",sayac1,"Ler")
    while(sayac2<11):
        print(sayac1,"X",sayac2,"=",sayac1*sayac2)
        sayac2=sayac2+1
    print("------------------------------------------------")
    sayac1=sayac1+1
print("Program bitti")
