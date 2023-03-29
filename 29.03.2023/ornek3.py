#ekrana aşağıdaki şekli Kullanıcının girdiği sayıya göre cizdiren program
#*
#**
#***
#****
#*****
#******
#*******
say=int(input("Sayı giriniz"))
for sayac1 in range(1,say+1,1):
    for sayac2 in range(1,sayac1+1,1):
                        print("*",end=" ")
    print("\n")

    
