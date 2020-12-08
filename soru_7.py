#BUBLE SORT ALGORITHM

def bubleSort(dizi):

    n = len(dizi)

    for i in range(0,n-1): #dizi içerisinde n-1. indekse kadar gezecek

        for j in range(0,n-i-1):

            if dizi[j]> dizi[j+1]:  #dizide j.değer kendisinden bir sonraki değerden büyükse yer değiştirecek ve büyük olan değer adım adım dizinin sağına doğru kayacak.
                                    #böylelikle her adımda dizinin elemanlarının sırası belli olmaya başlar.
                dizi[j],dizi[j+1] = dizi[j+1],dizi[j]

    return dizi

print("Siralanmis Dizi: "+ str(bubleSort([33,1,0,-2,2,4,3])))


            
