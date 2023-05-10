def azra():
    isim=input("Adınız ?")
    soyad=input("Soyadınız ?")
    yas=int(input("yaşınız"))
    print(isim,soyad,"adındaki vatandaş",yas," yaşındadır")
    if(yas<18):
        print("Ehliyet almaz")
    else:
        print("Ehliyet alabilir")

azra()
print("Program bitti")
