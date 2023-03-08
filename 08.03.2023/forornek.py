#Girilen adı 10 defa ekrana yazar
isim=input("Adınız nedir")
for say in range(10): print(isim)
#Girilen adı istenildiği kadar ekrana yazar
isim=input("Adınız nedir")
sayi=int(input("Kaç kez yazayım"))
for say in range(sayi): print(isim)
#1 den başlayıp girilen sayıya kadar olan sayıları toplayan program
topla=0
sayi=int(input("Kaç Kadar toplayayım"))
for say in range(sayi): topla=topla+say
print("sonuç =",topla)

