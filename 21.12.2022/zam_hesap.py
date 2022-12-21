#Ürünün mevcut fiyatı ve zam yüzdesini alarak oluşan yeni fiyatı veren program
Mevcut=int(input("Ürünün fiyatını girin"))
yuzde=int(input("Zam yuzdesini girin"))
yeni_fiyat=Mevcut+((Mevcut/100)*yuzde)
print("YEni Fiyat=",yeni_fiyat)
