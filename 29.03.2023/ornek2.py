#Kullanıcının girdiği sayıya kadar olan sayıların
#for ile çarpımını bulan
#çarpım bir önceki sonuctan büyükse büyük küçükse küçük eşitse eşit yazan
#Kullanıcı istediği sürece işlemyepmaya devem eden
#programı yazınız
tercih=1
onceki_sonuc=0
while(tercih==1):
    sayi=int(input("Çarpımı bulanacak sayıyı giriniz"))
    carpim=1
    for sayac in range(1,sayi+1,1):
        carpim=carpim*sayac
    if carpim >onceki_sonuc :
        print("Çarpım büyük")
    elif carpim<onceki_sonuc:
        print("Çarpım küçük")
    else :
        print("çarpım eşit")
    onceki_sonuc=carpim
    tercih=int(input("Devam etmek için 1 bitirmek için 0 basın"))
print("Döngü sona erdi")
