class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = dict()
        for i, num in enumerate(nums):
            if target - num in pre:
                return [pre[target - num], i]
            # 同一个元素只记录最小的索引(去掉elif也不影响结果)
            elif num not in pre:
                pre[num] = i
        return []
