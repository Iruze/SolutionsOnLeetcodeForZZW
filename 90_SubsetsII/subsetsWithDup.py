class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(first=0, cur=[]):
            ans.append(cur[:])
            for i in range(first, len(nums)):
                if i - first > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, cur + [nums[i]])
        dfs()
        return ans
