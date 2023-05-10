#sıfırdan başlayarak kullanıcının girdiği sayıya kadar olan sayıları ekrana
#yazan fonksiyon örneği

#parametresiz
def yaz():
    sayi=int(input("sayı giriniz"))
    for x in range(0,sayi+1):
        print(x)
#parametreli 
def yaz2(sayi):
    for x in range(0,sayi+1):
        print(x)

print("Parametresiz fonsyon ile çözüm")
yaz()
print("Parametreli  fonksiyon ile çözüm")
sayi=int(input("sayı giriniz"))
yaz2(sayi)
print("9c matematikten anlamaz bitti")
