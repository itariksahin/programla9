sozluk={"Adınız":"MELİSAGÜL","Soyadınız":"KURU","Yaşınız":13,"TAKMA_ADINIZ":"BİŞEYDEMEZLER"}
print(sozluk)
#Anahtar değerleri yazdıralım
print(sozluk.keys())
#value(degerleri) yazdıralım
print(sozluk.values())
#anahtar değere karşılık gelen degerleri yazdıralım
print(sozluk["Yaşınız"])
#anahtara karşılık gelen değeri değiştime
sozluk["TAKMA_ADINIZ"]="GIÇIK"
print(sozluk)
print("-------------------------------------------------------\n")
#yeni anahtar ve deger ekleme
sozluk["EN_NEFRET_ETTİGİ"]="BEYZA"
print(sozluk)
print("-------------------------------------------------------\n")
#sozlukden anahtar ve deger silme
sozluk.pop("Soyadınız")
print(sozluk)
print("-------------------------------------------------------\n")
#sozluğün kopyasını oluşturma
yeni_ramazan=sozluk.copy()
print("SÖZLÜK=",sozluk)
print("YENİ SÖZLÜK=",yeni_ramazan)
print("-------------------------------------------------------\n")
#Sözlüğün içeriğini silme
sozluk.clear()
print(sozluk)
print(yeni_ramazan)
print("-------------------------------------------------------\n")
#sözlüğü tamamen silme
del yeni_ramazan
print(yeni_ramazan)

