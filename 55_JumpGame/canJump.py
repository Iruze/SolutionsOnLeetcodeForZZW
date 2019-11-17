# Solution1: 贪心算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastBingo = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= lastBingo:
                lastBingo = i
        return lastBingo == 0
        
# Solution2: 动态规划（自底向上）
enum Idx {
    BAD, UNKNOWN, GOOD
}

class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        
        Idx[] dp = new Idx[n];
        for(int i = 0; i < n; ++i)
            dp[i] = Idx.UNKNOWN;
        dp[n - 1] = Idx.GOOD;
        
        for(int i = n - 2; i >= 0; --i) {
            int furthestIdx = Math.min(n - 1, nums[i] + i);
            for(int j = i + 1; j <= furthestIdx; ++j) {
                if(dp[j] == Idx.GOOD) {
                    dp[i] = Idx.GOOD;
                    break;
                }
            }
        }
        
        return dp[0] == Idx.GOOD;
    }
}
