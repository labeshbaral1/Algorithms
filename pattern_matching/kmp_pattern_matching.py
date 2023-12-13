#returns the indcies of all occurences of P in T
#Preprocessing must compute LPS Array in O(m) Time and O(m) space
#Time Complexity is O(n+m) total

def KMP_search(P, T):
    M, N = len(P), len(T)
    lps = [0] * M
    j = 0
    computeLPSArray(P, M, lps)
    i = 0
    result = []  
    while i < N:
        if P[j] == T[i]:
            i += 1
            j += 1
        if j == M:
            result.append(i - j)  
            j = lps[j - 1]
        elif i < N and P[j] != T[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result  

def computeLPSArray(P, M, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < M:
        if P[i] == P[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

print(KMP_search("na", "banana"))



