#Girilen 10 derse göre ortalama ve belge hesaplayan program
ders1=int(input("matemetik notunu giriniz"))
ders2=int(input("türkçe notunu giriniz"))
ders3=int(input("İngilizce notunu giriniz"))
ders4=int(input("Fizik notunu giriniz"))
ders5=int(input("Kimya notunu giriniz"))
ders6=int(input("tarih notunu giriniz"))
ders7=int(input("Coğrafya notunu giriniz"))
ders8=int(input("Din kültürü notunu giriniz"))
ders9=int(input("Beden eğitimi notunu giriniz"))
ders10=int(input("Biyoloji notunu giriniz"))
ortalama=(ders1+ders2+ders3+ders4+ders5+ders6+ders7+ders8+ders9+ders10)/10
if ortalama<25 : print("ortalamanız",ortalama,"tastik name almaya hak kazandınız")
elif ortalama<50: print("ortalamanız",ortalama,"Sınıfta kaldınız")
elif ortalama<70:print("ortalamanız",ortalama,"Onur belgesi alma imkanınız var")
elif ortalama<85:print("ortalamanız",ortalama,"teşekkür belgesi aldınız")
elif ortalama<101:print("ortalamanız",ortalama,"Takdir belgesi aldınız")
else : print("ortalamanız",ortalama,"Ortalama 100 den büyük olamaz")
          
