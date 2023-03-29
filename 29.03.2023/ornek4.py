#ekrana aşağıdaki şekli Kullanıcının girdiği sayıya göre cizdiren program
#****
#***
#**
#*
say=int(input("Sayı giriniz"))
for sayac1 in range(say,0,-1):
    for sayac2 in range(sayac1,0,-1):
                        print("*",end=" ")
    print("\n")
