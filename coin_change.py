def coinChange(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for coin in coins:
            if i - coin>=0:
                dp[i]=min(dp[i],dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1
print("output for [1,2,5],11:",coinChange([1,2,5],11))
print("output for [2],3:",coinChange([2],3))
print("output for [1],0:",coinChange([1],0))

              
