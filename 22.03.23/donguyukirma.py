#break komutu dögüyü bitirir ve çıkar
#continue komutu döngünün sadece o aşamasını atlar
i=0
while i<100:
    if(i%5==0):print("SAyı beşin katı oldu için atlandı")
    else:print(i)
    soru=input("Devam edilsin mi e-evet h-hayır için seçiniz")
    if(soru=="h"):break
    i=i+1
print("döngü bitti")
