class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        edge = sum(nums) // 4
        if edge * 4 != sum(nums) or edge < max(nums):
            return False
        sums = [0] * 4
        # 贪心思想：优先将大的边放入到sums中去
        nums.sort(reverse=True)
        def dfs(idx=0):
            nonlocal edge
            if idx == len(nums):
                return sums[0] == sums[1] == sums[2] == edge
            # 回溯思想：挨个将边nums[idx]放入到四条边中去尝试
            for i in range(4):
                if sums[i] + nums[idx] <= edge:
                    sums[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    sums[i] -= nums[idx]
            # 四条边都试过了都不行，则false退出
            return False
        
        return dfs()
