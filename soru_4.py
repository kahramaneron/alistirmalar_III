#INSERTION ALGORITHM

def Insertion(dizi):

    for i in range(1,len(dizi)):

        key = dizi[i]
        j = i-1

        while(key < dizi[j] and j>=0):
            dizi[j+1] = dizi[j]
            j -= 1
            

        else:
            dizi[j+1]=key



dizi = [11,7,15,3,16,13]
Insertion(dizi)

print("Siralanmis Dizi: ")

for i in range(len(dizi)):
    print("%d" %dizi[i], end = " ")
