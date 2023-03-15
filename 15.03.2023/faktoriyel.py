#Kullanıcının girdiği sayının faktöriyelini hesaplayan program
sonuc=1
sayac=1
faktoriyel=int(input("HAngi sayının faktöriyeli hesaplansın"))
while(sayac<=faktoriyel):
    sonuc=sonuc*sayac
    sayac=1+sayac
print("Faktöriye degeri=",sonuc)
