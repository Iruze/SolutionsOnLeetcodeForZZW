# 解法一： 递归-回溯： 交换nums
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output


# 解法二：递归-回溯：visited记录访问足迹
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _dfs(depth=0, cur=[]):
            if depth == len(nums):
                output.append(cur[:])
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    cur.append(nums[i])
                    _dfs(depth + 1, cur)
                    cur.pop()
                    visited[i] = False
        output = []
        visited = [False for _ in range(len(nums))]
        _dfs()
        return output
