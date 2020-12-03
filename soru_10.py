

def quickSort(dizi, alt, üst):
    pivot = dizi[üst]
    i = alt-1

    for j in range(alt,üst):

        if dizi[j]< pivot:
            i = i+1
            dizi[i],dizi[j] = dizi[j],dizi[i]

    dizi[i+1],dizi[üst] = dizi[üst],dizi[i+1]
    return(i+1)

def sort(dizi, alt, üst):

    if alt < üst:

        böl= quickSort(dizi,alt,üst)
        sort(dizi,alt, böl-1)
        sort(dizi,böl+1, üst)


dizi = [3,7,1,5,8,2]
sort(dizi,0,len(dizi)-1)

print("Siralanmis Dizi: ")

for i in range(len(dizi)):
    print("%d" %dizi[i], end=" ")
