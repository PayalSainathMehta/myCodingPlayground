def addSubset(l, k):
    for i in range(len(l)):
        if k - l[i] in l:
            return True
    return False


l = [10,15,3,3]
k = 17
print(addSubset(l,k))
