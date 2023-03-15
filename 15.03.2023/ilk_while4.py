#Kullanıcının girdiği sayıya kadar olan sayıların tek mi çift mi olduğunu bulan program
sayi_al=int(input("Kaça kadar bakayım"))
i=1
while(i<=sayi_al):
    if(i%2==0):
        print(i,"- Çift sayıdır")
    else:
        print(i,"- tek sayıdır")
    i=i+1
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
