#ODD-EVEN SORT ALGORITHM

def oddEvenSort(dizi):
    n=len(dizi)
    degisim=True    #algoritmayi kontrol edebilmek adina boolean degerimizi belirledik

    while(degisim==True):
        degisim=False   #algoritmamizin dogru loopa girebilmesi icin buraya ekledik

        for i in range(0,n-1,2):    #1.adimda çift indisli elemanlari karsilastirdik ve büyük olanlari saga dogru hareket ettirdik.
            if dizi[i] > dizi[i+1]:
                dizi[i],dizi[i+1]=dizi[i+1],dizi[i]
                degisim=True

        for i in range(1,n-1,2):    #2.adimda tek indisli elemanlari kiyasladik ve büyük olanlari saga dogru hareket ettirdik.
            if dizi[i] > dizi[i+1]:
                dizi[i],dizi[i+1]=dizi[i+1],dizi[i]
                degisim=True

    return dizi

print("Siralanmis Dizi: "+ str(oddEvenSort([3,7,4,5,1,0])))
