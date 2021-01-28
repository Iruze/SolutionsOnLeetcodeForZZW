class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        if(nums != null && nums.length >= 3)
        {
            Arrays.sort(nums);
            
            int resultOfDiff = Integer.MAX_VALUE;
            int allDiff = Integer.MAX_VALUE;
            for(int left = 0; left < nums.length - 2; left++)
            {
                int middle = left + 1;
                int right = nums.length - 1;
                
                while(middle < right)
                {
                    int sum = nums[left] + nums[middle] + nums[right];
                    int tempDiff = sum - target;
                    
                    allDiff = minAbsCompare(tempDiff, allDiff);
                    
                    if(sum > target)
                        right--;
                    else if(sum < target)
                        middle++;
                    else
                        return sum;
                }
                
                resultOfDiff = minAbsCompare(allDiff, resultOfDiff);
            }
            
            return (resultOfDiff + target);
        }
        
        return Integer.MIN_VALUE;
    }
    
    public int minAbsCompare(int num1, int num2)
    {
        if(Math.abs(num1) < Math.abs(num2))
            return num1;
        else
            return num2;
    }
}
