class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)
        ans = 0
        for idx, cita in enumerate(citations):
            if citations[idx] >= idx + 1:
                ans = idx + 1
            # idx之后所有的已引用的篇数，大于当前数篇的引用数nums[idx]，必然不是h
            else:               
                break
        return ans
