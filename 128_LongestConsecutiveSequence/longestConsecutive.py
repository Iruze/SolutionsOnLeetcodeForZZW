class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 复杂度为O(n)， 最坏为O(2n)， 当连续序列的起始值为nums[-1]
        #, 这样相当于遍历到nums结尾之后，需要再一次一次遍历nums
        longest_size = 0
        nums_set = set(nums)
        for num in nums_set:
            # 试探性地找到连续序列的最小（起始）值
            if num - 1 not in nums_set:
                cur_num = num
                cur_size = 1
                # 在起始值中往上递增，探索最长连续子序列
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_size += 1
                longest_size = max(longest_size, cur_size)
        return longest_size
