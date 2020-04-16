"""
我们定义f ( i ) 和 g ( i )，其中 f( i ) 表示不删除元素的情况下最大子数组和（区间为[0，i]），g( i ) 
代表删除元素的情况下的最大子数组和（区间为[0，i]）。

f(i) = Math.max(f(i-1)+arr[i],arr[i]) //要么是当前元素累加之前的和，要么是重新从当前元素开始
g(i) = Math.max(g(i-1)+arr[i],f(i-1)) 
//要么是加上当前元素，也就是维持之前删除某个元素的情形，即g[i-1]+arr[i]
//要么是删除当前这个元素，那么区间[0, i-1]就是不删除元素的情况，即f(i-1)+0（注意是f不是g！！）

"""

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = arr[0]
        # 注意，dp[0][1]的取值尽可能小
        dp[0][1] = -float('Inf')
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0])
        return max(max(d) for d in dp)
