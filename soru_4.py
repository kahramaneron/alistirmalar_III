#INSERTION SORT ALGORITHM

def insertionSort(dizi):

    for i in range(1,len(dizi)):

        key = dizi[i]
        j = i-1

        while(key < dizi[j] and j>=0):
            dizi[j+1] = dizi[j]
            j -= 1
            

        else:
            dizi[j+1]=key


    return dizi

print("Siralanmis Dizi: " + str(insertionSort([7,11,15,13,16,3])))
