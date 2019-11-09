from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        privot = reduce(lambda x, y: x ^ y, nums)
        digit = 0
        while privot and not (privot & 1):
            digit += 1
            privot = privot >> 1
        r1, r2 = 0, 0
        for num in nums:
            if (num >> digit) & 1:
                r1 = r1 ^ num
            else:
                r2 = r2 ^ num
        return [r1, r2]
