class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0 : 1}
        ssum, count = 0, 0
        for num in nums:
            ssum += num
            count += d.get(ssum - k, 0)
            d[ssum] = d.setdefault(ssum, 0) + 1
        return count
