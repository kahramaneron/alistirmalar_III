

def bubleSort(dizi):

    n = len(dizi)

    for i in range(0,n-1): 

        for j in range(0,n-i-1):

            if dizi[j]> dizi[j+1]:

                dizi[j],dizi[j+1] = dizi[j+1],dizi[j]

            j +=1


    return dizi


print("Siralanmis Dizi: "+ str(bubleSort([33,1,0,-2,2,4,3])))


            
