class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        ans = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            s = set()
            for num in nums:
                s.add(mask & num)
            temp = ans | (1 << i)
            for prefix in s:
                if temp ^ prefix in s:
                    ans = temp
        return ans
