class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if idx < 2 or num != nums[idx - 2]:
                nums[idx] = num
                idx += 1
        return idx
        
        
        
""""""""""""""""""""""""""""""""""""""""""""""""""""""
                      -通用模板-
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 如果改成：“最多重复k个元素”
class Solution:
    def removeDuplicates(self, nums， k):
        idx = 0
        for num in nums:
            if idx < k or num != nums[idx-k]:
                nums[idx] = n
                idx += 1
        return idx
"""
