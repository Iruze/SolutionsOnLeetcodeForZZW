# lru_cache(None)的应用
- 用法
```python
from functools import lru_cache

@lru_cache(None)
def func(l, r):
    pass
```
其中, `None`是形参`maxsize=None`的缩写, 入口参数`l`, `r`
必须是`immutable`, 即**可哈希的**.

#### 例题
- [887. 鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop/)
> 你将获得 `K` 个鸡蛋，并可以使用一栋从 `1` 到 `N`  共有 `N` 层楼的建筑。
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 `F` ，满足 `0 <= F <= N` 任何从高于 `F` 的楼层落下的鸡蛋都会碎，从 `F` 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 `X` 扔下（满足 `1 <= X <= N`）。
你的目标是确切地知道 `F` 的值是多少。
无论 `F` 的初始值如何，你确定 `F` 的值的最小移动次数是多少？
```shell script
输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
```

- 参考:

[labuladong-题目理解 + 基本解法 + 进阶解法](https://leetcode-cn.com/problems/super-egg-drop/solution/ji-ben-dong-tai-gui-hua-jie-fa-by-labuladong/)

[labuladong-算法小抄(高楼扔鸡蛋)]()

<details>
    <summary>解法一: 传统dp</summary>
    
```python
# 时间复杂度 O(KN * N), 空间复杂度 O(KN)
@lru_cache(None)
def dp(K, N):
    # base case
    if K == 1: return N
    if N == 0: return 0
    ans = float('Inf')
    # 最坏情况下的最少扔鸡蛋次数, 逐层遍历, 穷举所有的可能
    for i in range(1, N + 1):
        ans = min(ans, 
                max(
                    dp(K, N - i),      # 在i层没碎了
                    dp(K - 1, i - 1)   # 碎了
                    ) + 1
                )
    return ans
``` 
</details>

<details>
    <summary>解法二: 二分dp</summary>
    
```python
# 时间复杂度 O(KN * logN), 空间复杂度 O(KN)
@lru_cache(None)
def dp(K, N):
    if K == 1: return N
    if N == 0: return 0
    ans = float('Inf')
    lo, hi = 1, N
    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        broken = dp(K - 1, mid - 1)  # 碎
        not_broken = dp(K, N - mid)  # 没碎
        # ans = min(max(碎, 没碎) + 1)
        if broken > not_broken:
            hi = mid - 1
            ans = min(ans, broken + 1)
        else:
            lo = mid + 1
            ans = min(ans, not_broken + 1)
    return ans
``` 
</details>


给你 K 个鸡蛋，测试 m 次， 最坏情况下最多能测试 N 层楼.

dp的定义基于下面这两个事实:
> ⽆论你在哪层楼扔鸡蛋， 鸡蛋只可能摔碎或者没摔碎， 碎了的话就测楼
下， 没碎的话就测楼上。

> ⽆论你上楼还是下楼， 总的楼层数 = 楼上的楼层数 + 楼下的楼层数 +
1（当前这层楼）。

可以写出下⾯的状态转移⽅程：
````shell script
dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1
````

<details>
    <summary>解法三: 重新定义dp</summary>
    
```python
# 时间复杂度 O(KN), 空间复杂度 O(KN)
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(K, M):
            # 因为K<=M, 所以K=1的时候M=0或者M=1
            if K == 1 or M == 1: return M
            return dp(K - 1, M - 1) + dp(K, M - 1) + 1
        
        M = 1
        while dp(K, M) < N:
            M += 1
        return M
``` 
</details>

- [375. 猜数字大小 II](https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/)
> 我们正在玩一个猜数游戏，游戏规则如下：
我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。
每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。
然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。

<details>
    <summary>解题思路</summary>
    
```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:

        # # 方法一: 记忆化递归
        # from functools import lru_cache

        # @lru_cache(None)
        # def helper(l, r):
        #     if r - l <= 0: return 0
        #     if r - l == 1: return l
        #     if r - l == 2: return l + 1
        #      """
        #      从(l, (r + l) / 2)内选择数字作为第一次尝试, 右边区间都比左边区间大,开销肯定大于左边, 总体开销也较大
        #      所以, 从((l + r) / 2, r)内选择, 这样两个区间的开销更接近, 且总体开销会更小
        #      """
        #     return min(x + max(helper(l, x - 1), helper(x + 1, r)) for x in range((l + r) >> 1, r + 1))
        # return helper(1, n)

        # 方法二: dp方法, 将上述递归改为dp
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            dp[i][i + 1] = i
        for l in range(n + 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(x + max(dp[l][x - 1], dp[x + 1][r]) for x in range((l + r) >> 1, r))
        return dp[1][n]
``` 
</details>


- [132. 分割回文串 II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)
> 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的最少分割次数。

示例:
```shell script
输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
```

<details>
    <summary>解题思路</summary>
    
```python
import functools


class Solution:
    @functools.lru_cache(None)
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        ans = float('Inf')
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                ans = min(ans, self.minCut(s[i:]) + 1)
        return ans
``` 
</details>


- [312. 戳气球](https://leetcode-cn.com/problems/burst-balloons/)
> 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。

示例:
```shell script
输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

说明:
````shell script
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
````

<details>
    <summary>解题思路</summary>
    
```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import lru_cache

        nums = [1] + nums + [1]

        @lru_cache(None)
        def dfs(lo, hi):
            if hi - lo < 2:
                return 0
            return max(nums[lo] * nums[i] * nums[hi] + dfs(lo, i) + dfs(i, hi) for i in range(lo + 1, hi))

        return dfs(0, len(nums) - 1)
```
</details>

- [174. 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/)

<details>
    <summary>解题思路</summary>
    
```python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        # dp = [[0] * cols for _ in range(rows)]
        # dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        # for r in range(rows - 1, -1, -1):
        #     for c in range(cols - 1, -1, -1):
        #         if r == rows - 1 and c == cols - 1: 
        #             continue
        #         elif r == rows - 1:
        #             dp[r][c] = max(1, dp[r][c + 1] - dungeon[r][c])
        #         elif c == cols - 1:
        #             dp[r][c] = max(1, dp[r + 1][c] - dungeon[r][c])
        #         else:
        #             dp[r][c] = max(1, min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c])
        # return dp[0][0]
        
        @functools.lru_cache(None)
        def dp(i, j):
            if i == rows - 1 and j == cols - 1:
                return max(1, 1 - dungeon[i][j])
            if i == rows - 1:
                return max(1, dp(i, j + 1) - dungeon[i][j])
            if j == cols - 1:
                return max(1, dp(i + 1, j) - dungeon[i][j])
            return max(1, min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j])
        return dp(0, 0)
``` 
</details>
















