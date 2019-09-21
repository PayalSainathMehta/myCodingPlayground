def diStringMatch(S):
    n = len(S)
    A = []
    inc = 0
    dec = n
    for i in range(0,n):
        if S[i] == 'I':
            A.append(inc)
            inc+=1
        else:
            A.append(dec)
            dec-=1

    A.append(dec)
    return A


print(diStringMatch('IDID'))
            
