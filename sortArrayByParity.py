def sortArrayByParity(self, a):
    i = 0
    j =0
    while j < len(a):
        if a[j]%2==0:
            a[i],a[j] = a[j],a[i]
            i+=1
            j+=1
    return a