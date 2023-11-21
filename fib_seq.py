#dp implementation of fib numeber to find the fib number in O(n)
#Time Compleixty O(n)
#Space Complexity O(n)
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
