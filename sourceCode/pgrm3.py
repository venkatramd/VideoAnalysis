str="2345"

def remsbtr(S,i,j):
    S = (S[:i-1] + S[j:])
    return S

for i in range(0,len(str)-1):
    for j in range(0,len(str)-i):
        sstr=remsbtr(str,j,j+i)
        print(sstr)


