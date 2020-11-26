//  自底向上
class Solution {
    public boolean canJump(int[] nums) {
        int start = nums.length - 2, end = nums.length - 1;
        while(start >= 0) {
            if(start + nums[start] >= end) {
                end = start;
            }

            --start;
        }

        return end <= 0;
    }
}



// 自顶向下
class Solution {
    public boolean canJump(int[] nums) {
        int end = 0;
        for(int i = 0; i < nums.length; ++i) {
            if(end < i) {
                return false;
            }
            end = Math.max(end, i + nums[i]);
            if(end >= nums.length - 1) {
                return true;
            }
        }

        return false; 
    }
}
