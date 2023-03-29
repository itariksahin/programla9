#kullanıcının girdiği sayının toplamını kullanıcının sectiği döngü ile bulan
#ve kullanıcı istediği sürece istediği döngü ile hesaplamaya devam eden program
secim="e"
while (secim=="e") :
    toplam=0
    sayi=int(input("kaça kadar toplama işlemi yapılacak"))
    tercih=input("For için-f,while için w secin")
    if tercih=="f":
            for sayac in range(sayi+1):
                toplam=toplam+sayac
    elif tercih=="w":
            sayac=1
            while(sayac<=sayi):
                toplam=toplam+sayac
                sayac=sayac+1
    else :print("Yanlış tercih yaptınız")
    print("Toplam sonucu=",toplam)
    secim=input("Devam edilsin mi?evet için e haır için h seciniz")
print("Program bitti")
        
