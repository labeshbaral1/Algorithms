#returns the index of the positions containing the pattern P wihtin a text T using hashing rules
#Worse Case Time complexity is O(nm)
#Space Complexity is O(1)
def rabin_karp_search(pat, txt, q):
    d = 256
    M, N = len(pat), len(txt)
    p, t, h = 0, 0, 1
    result = []

    for i in range(M-1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
            else:
                result.append(i)

        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

    return result


print(rabin_karp_search("ban", "bananaban", 10))