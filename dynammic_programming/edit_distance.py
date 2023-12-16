#dp algorhtm that determeins the edit distance between two strings using a bottom up approach
#Time complexity is O(mn)
#Space complexity is 0(mn)
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      
                                   dp[i-1][j],     
                                   dp[i-1][j-1])    

    return dp[m][n]

def ED(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    
    if str1[-1] == str2[-1]:
        return ED(str1[:-1], str2[:-1])

    return 1 + min(ED(str1, str2[:-1]),   
                   ED(str1[:-1], str2),   
                   ED(str1[:-1], str2[:-1])
                  )


print(ED("abba", "caba"))

