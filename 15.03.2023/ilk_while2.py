#kullanıcıdan adınını soyadını alan ve bunları kullanıcının istediği kadar ekrana yazan program
ad=input("Adımızı giriniz")
soyad=input("Soyadınızı giriniz")
tur=int(input("Kaç kez yazayım"))
i=0
while(i<=tur):
 print(ad+" "+soyad)
 i=i+1
print("*************************")
