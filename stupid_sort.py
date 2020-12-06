

def stupidSort(dizi):
    n = len(dizi)
    degisim = True      #dizinin elemanlari arasinda degisim olup olmadigini kontrol etmek icin boolean deger dönülür

    while(degisim==True):
        degisim=False

        for i in range(0,n-1):

            if dizi[i] > dizi[i+1]:     #büyük olan sayi her seferinde saga dogru itilecek
                dizi[i],dizi[i+1]=dizi[i+1],dizi[i]
                degisim = True

            if degisim==True:   #degisim meydana geliyorsa indis sifirdan baslayacak
                i=0

            i = i+1


    return dizi

print("Siralanmis Dizi: "+str(stupidSort([7,9,1,8,3])))
