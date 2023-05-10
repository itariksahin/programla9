#Sınıf not ortalamasını hesaplayan program
sinif_Sayisi=int(input("sınıftaki öğrenci sayısını giriniz"))
sayac=0
toplam=0
while(sayac<sinif_Sayisi):
    print(sayac+1,".öğrenci notunu giriniz")
    not1=int(input(""))
    toplam=toplam+not1
    sayac=sayac+1
ortalama=toplam/sinif_Sayisi
print("Sınıfın ortalaması=",ortalama)
print("Program bitti")
    
