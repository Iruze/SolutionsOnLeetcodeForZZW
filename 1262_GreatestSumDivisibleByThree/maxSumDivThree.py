""" 解题思路：
不妨设dp[i] 代表 选取的数字累加和 模3 = i 的数字和     
假定nums[i] % 3 = 1 ，那么，和 前面选取的数字和模 3 = 2 的数相加，就可以模3为 0 ，表达起来就是 dp[0] = max(dp[0], nums[i] + dp[2])      
依次类推，只要不断更新 dp 数组即可，注意一点，更新的时候要保存上一个状态的值，避免后续更新的时候重复影响。      
"""
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            # if num % 3 == 0:
            #     dp[0] = max(dp[0], dp[0] + num)
            #     dp[1] = max(dp[1], dp[1] + num)
            #     dp[2] = max(dp[2], dp[2] + num)
            # if num % 3 == 1:
            #     dp[0] = max(dp[0], dp[2] + num)
            #     dp[1] = max(dp[1], dp[0] + num)
            #     dp[2] = max(dp[2], dp[1] + num)
            # if num % 3 == 2:
            #     dp[0] = max(dp[0], dp[1] + num)
            #     dp[1] = max(dp[1], dp[2] + num)
            #     dp[2] = max(dp[2], dp[0] + num)
            dp = [max(dp[i], dp[(i - num) % 3] + num) for i in range(3)]
        return dp[0]
        
"""
有问题的地方：
1). 初始值dp = [0, float('-Inf'), float('-Inf')]，为什么不是dp = [0, 0, 0]
2). dp[(i - num) % 3]，有的解法是 dp[(3 + i - mod) % 3], 或者dp[(i - mod) % 3], 这里需要运用到的取余运算为：
    (a + b) % p = (a % p + b % p) % p 

    (a - b) % p = (a % p - b % p) % p 

    (a * b) % p = (a % p * b % p) % p 
<参考：https://blog.csdn.net/ash_zheng/article/details/38541777>

一定要保存上一次的dp数组结果，当前次参与的dp[i]是上一次的结果，跟本次的不能混淆
a). if num % 3 == 0，这种写法混淆了当前次和上一次的结果，答案错误
b). dp = [max(dp[i], dp[(i - num) % 3] + num) for i in range(3)]
    这种，先运算[]里面的部分，后赋值给dp，所以[]里面参与运算的dp是上一次的， 答案正确
"""
