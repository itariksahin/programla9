# Girilen iki sayı arasındaki sayıların toplamını bularak ekrana yazdırınız.
sayi1=int(input("ilk sayıyı giriniz"))
sayi2=int(input("İkinci sayıyı giriniz"))
toplam=0
for sayac in range(sayi1,sayi2+1): toplam=toplam+sayac
print("Toplam=",toplam)
# Girilen iki sayının arasındaki sayıların ortalamasını bularak ekrana yazdırınız.
sayi1=int(input("ilk sayıyı giriniz"))
sayi2=int(input("İkinci sayıyı giriniz"))
toplam=0
for sayac in range(sayi1,sayi2+1): toplam=toplam+sayac
ortalama=toplam/(sayi2+1-sayi1)
print("Ortalama=",ortalama)
# Girilen sayının faktöriyelini bularak ekrana yazdırınız.
faktor=1
sayi1=int(input("Faktoriyeli alınacak sayıyı giriniz"))
for sayac2 in range(1,sayi1+1):faktor=faktor*sayac2
print("Sonuç=",faktor)
