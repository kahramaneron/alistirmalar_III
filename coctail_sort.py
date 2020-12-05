#COCTAIL SORT ALGORITHM


def coctailSort(dizi):
    n= len(dizi)
    degisim = True  #dizi içerisinde degisikligin meydana gelip gelmedigini kontrol etmek amaciyla boolean deger donuyoruz.
    baslangic=0
    bitis=n-1

    while(degisim==True):
        degisim=False   #döngü içerisine girmeden önce kontrol mekanizmamizi sifirliyoruz

        for i in range(baslangic,bitis):
            if dizi[i] > dizi[i+1]:
                dizi[i],dizi[i+1]=dizi[i+1],dizi[i] #soldan saga 'Buble Sort'taki gibi siraliyoruz.
                degisim=True

        if(degisim==False):     #eger hiçbir sey hareket etmediyse dizi siralanmis demektir.
            break

        degisim=False

        bitis = bitis-1     #bitisi 1 azalttik cunku en sondaki eleman ilk loopumuzda yerine yerlesmis olacak

        for i in range(bitis-1,baslangic-1,-1):
            if dizi[i] > dizi[i+1]:
                dizi[i],dizi[i+1]=dizi[i+1],dizi[i] #bu sefer sagdan sola BubleSort islemini tekrarliyoruz.
                degisim=True

        baslangic = baslangic+1 #bu kisimda da baslangiçtaki elemanlar yerini almis olacak

    
    return dizi

print("Siralanmis Dizi: "+ str(coctailSort([4,1,3,8])))

                
                
