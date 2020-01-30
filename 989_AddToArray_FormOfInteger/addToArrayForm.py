# 解法一： list转化为整数 -> 相加 -> 对和list化
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = [str(v) for i, v in enumerate(A)]
        A = int(''.join(A))
        res = list(str(A + K))
        return [int(v) for v in res]
        
        
# 解法二：  模拟十进制加法
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i = len(A) - 1
        K = str(K)
        j = len(K) - 1
        res = []
        carry = 0
        while i >= 0 or j >= 0:
            n1 = A[i] if i >= 0 else 0
            n2 = int(K[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res.insert(0, tmp % 10)
            i, j = i - 1, j - 1
        if carry:
            res = [1] + res
        return res
