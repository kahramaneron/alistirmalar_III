

def selectionSort(dizi):

    for i in range(0,len(dizi)):
        ind = i

        for j in range(i+1,len(dizi)):

            if dizi[j] < dizi[ind]:
                ind = j

        dizi[i],dizi[ind]= dizi[ind],dizi[i]


dizi = [3,2,1,4]
selectionSort(dizi)

print("Siralanmis Dizi: ")

for i in range(0,len(dizi)):
    print("%d" %dizi[i], end=" ")
