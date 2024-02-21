def insertion(nbr):
    for i in range(1,len(nbr)):
        temp=nbr[i]
        j=i-1
        while j>=0 and temp <nbr[j]:
            nbr[j + 1]= nbr[j]
            j=j-1
        nbr[j+1]=temp
n=int(input('enter the nbr of element '))
nbr=[]
for i in range(0,n):
    c=int(input("enter the numbers "))
    nbr.append(c)
insertion(nbr)
print('the values after insertion',nbr)
