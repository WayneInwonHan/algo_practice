def checkIfExist(self, arr):
    N = len(arr)
    for i in range(N):
        try:
            if arr.index(arr[i]*2)!=i:
                return True
        except:
            continue
    return False