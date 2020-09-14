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