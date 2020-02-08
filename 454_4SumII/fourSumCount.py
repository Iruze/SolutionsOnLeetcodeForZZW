# 解法一：用 defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        h = collections.defaultdict(int)
        for a in A:
            for b in B:
                h[- a - b] += 1
        return sum(h[c + d] for c in C for d in D if c + d in h)
        
# 解法二： 用collections.Counter()
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        h = collections.Counter(- a - b for a in A for b in B)
        return sum(h[c + d] for c in C for d in D)
