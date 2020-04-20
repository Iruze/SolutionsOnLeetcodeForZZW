# 参考：https://leetcode-cn.com/problems/super-pow/solution/you-qian-ru-shen-kuai-su-mi-suan-fa-xiang-jie-by-l/
class Solution:

    def __init__(self):
        self.base = 1337

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = self.myPow(a, last)
        part2 = self.myPow(self.superPow(a, b), 10)
        return part1 * part2 % self.base
    
    def myPow(self, a, k):
        a %= self.base
        res = 1
        for _ in range(k):
            res *= a
            res %= self.base
        return res
