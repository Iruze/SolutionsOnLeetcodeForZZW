# 解法一：递归-回溯：交换nums
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def _backtrack(first=0):
            if first == len(nums):
                output.append(nums[:])
            for i in range(first, len(nums)):
                if nums[i] not in nums[first:i]:
                    nums[i], nums[first] = nums[first], nums[i]
                    _backtrack(first + 1)
                    nums[i], nums[first] = nums[first], nums[i]
        output = []
        _backtrack()
        return output


# 解法二：递归-回溯：visited记录访问足迹
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def _dfs(depth=0, cur=[]):
            if depth == len(nums):
                output.append(cur[:])
            for i in range(len(nums)):
                if not visited[i]:
                    if 0 < i and nums[i - 1] == nums[i] and not visited[i - 1]:
                        continue
                    visited[i] = True
                    cur.append(nums[i])
                    _dfs(depth + 1, cur)
                    cur.pop()
                    visited[i] = False
        if not nums: 
            return []
        nums.sort()
        output = []
        visited = [False for _ in range(len(nums))]
        _dfs()
        return output
        
