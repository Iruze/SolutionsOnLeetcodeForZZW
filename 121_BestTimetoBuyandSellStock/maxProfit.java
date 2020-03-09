# 解法二： 状态机解法
class Solution {
    public int maxProfit(int[] prices) {
        
        if(prices.length <= 0)
            return 0;
        
        int dp_i_0 = 0;
        int dp_i_1 = Integer.MIN_VALUE;
        
        for(int i = 0; i < prices.length; i++)
        {
            dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
            dp_i_1 = Math.max(dp_i_1, 0 - prices[i]);
        }
        
        return dp_i_0;
    }
}
