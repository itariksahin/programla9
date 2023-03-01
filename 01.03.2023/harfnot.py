#Üniversitelerde gecerli harf notunu hesaplayab program
vizeNotu1 = float(input("1. Vize notu gir : "))
vizeNotu2 = float(input("2. Vize notu gir : "))
finalNotu = float(input("Final notu gir :"))
# Vize notlarının ortalamasının %40 ve Final puanının %60 ını hesaplayalım .
genelOrtalama = (((vizeNotu1+vizeNotu2)/2)*0.4) + (finalNotu*0.6)
print("Not ortalamanız : ", genelOrtalama)
# Koşul kısmına bir de final notunun 50'den büyük olmasını şart koşalım .
if finalNotu >= 50:

    if (genelOrtalama >= 85 and finalNotu >= 50):
        print("Harf Notunuz AA")
    elif genelOrtalama >= 75 and genelOrtalama < 85:
        print("Harf Notunuz BA")
    elif genelOrtalama >= 70 and genelOrtalama < 75:
        print("Harf Notunuz BB")
    elif genelOrtalama >= 65 and genelOrtalama < 70:
        print("Harf Notunuz CB")
    elif genelOrtalama >= 60 and genelOrtalama < 65:
        print("Harf Notunuz CC")
    elif genelOrtalama >= 55 and genelOrtalama < 60:
        print("Harf Notunuz DC")
    elif genelOrtalama >= 50 and genelOrtalama < 55:
        print("Harf Notunuz DD")

else:
    print("Harf notunuz FF kaldınız .")
