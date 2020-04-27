class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 只要 m < n，相与结果最低位一定是0
        # 使得 m, n 逼近，不断去处n的最低位的1
        while m < n:
            n = n & (n - 1)
        return n
