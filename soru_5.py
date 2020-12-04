#SELECTION SORT ALGORITHM

def selectionSort(dizi):

    for i in range(0,len(dizi)):
        ind = i

        for j in range(i+1,len(dizi)):

            if dizi[j] < dizi[ind]:
                ind = j

        dizi[i],dizi[ind]= dizi[ind],dizi[i]
    
    return dizi

print("Siralanmis Dizi: "+ str(selectionSort([3,2,1,4,0])))
