class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(first=0, cur=[]):
            ans.append(cur[:])
            for i in range(first, len(nums)):
                dfs(i + 1, cur + [nums[i]])
        dfs()
        return ans
