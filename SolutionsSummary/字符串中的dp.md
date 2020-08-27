# <公共子序列/子数组> 二维系列
- [583. 两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)
> 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例 1:
```
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
```

解题思路:
```shell
a). dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)], 这里定义dp的时候容易出错，是n2列，n1行
b). 从1开始双重循环  
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
c). 若 word1[i - 1] == word2[j - 1], 注意是第i, j个数组，故取i - 1, j - 1
       dp[i][j] = dp[i - 1][j - 1] + 1
    否则，dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```
<details>
    <summary>代码</summary>
    
```python3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        # 这里定义dp的时候容易出错，是n2列，n1行
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        # 从1开始循环
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 这里切记i,j同时回退1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 维持前一个结果的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return n1 + n2 - dp[-1][-1] * 2
```
</details>

再来看看子数组，子数组作为连续的，与子序列稍有不同
```shell
区别于子序列，在word1[i - 1] != word2[j - 1]时：
             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
     子数组，在word1[i - 1] != word2[j - 1]时，不做处理
          默认dp[i][j] = 0
```
- [718. 最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)
> 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例 1:
```shell
输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 
长度最长的公共子数组是 [3, 2, 1]。
```
<details>
    <summary>解题思路</summary>
    
```python3
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 没有else, 在A[i - 1] != B[j - 1]时，不做处理,默认dp[i][j] = 0
        return max(max(x) for x in dp)
```
</details>

其他同类题目：
- [712. 两个字符串的最小ASCII删除和](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/)
- [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence)
- [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)


# <最大上升子序列/最少未识别> 一维系列
- [300. 最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
> 给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
```shell
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
```

<details>
    <summary>解题思路</summary>
    
```python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1 for _ in range(n)]    # dp[i]表示：上升子序列最后一个元素为i时的长度
        for i in range(1, n):
            for j in range(i):        # 求得每一个dp[i]
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)   # 加上dp[i]本身长度1
        return max(dp)
```
</details>

- [面试题 17.13. 恢复空格](https://leetcode-cn.com/problems/re-space-lcci/)
> 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。        
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。                                
在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。            
假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。                                  

注意：本题相对原题稍作改动，只需返回未识别的字符数               

示例：
```shell
输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
```
[参考:dp+字典树两种解法](https://leetcode-cn.com/problems/re-space-lcci/solution/jian-dan-dp-trieshu-bi-xu-miao-dong-by-sweetiee/)

<details>
    <summary>解题思路</summary>
    
```python3
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = set(dictionary)
        n = len(sentence)
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1                  # 初始化dp[i], 默认sentence[i]不匹配
            for j in range(i):
                if sentence[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])      # 当j索引的字符同时被sentence[:j+1]和sentence[j:i]占用, 取两者最小的未识别数
        return dp[n]
```
</details>
