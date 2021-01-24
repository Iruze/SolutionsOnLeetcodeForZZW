class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 自定义排序规则
        def my_comparison(x, y):
            x, y = str(x), str(y)
            if x + y > y + x:
                return 1
            else:
                return -1
        # 逆序排列
        nums.sort(key=functools.cmp_to_key(my_comparison), reverse=True)
        nums = [*map(str, nums)]
        return ''.join(nums) if nums[0] != '0' else '0'

    
# 匿名函数解法
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [*map(str, nums)]
        nums.sort(key=functools.cmp_to_key(lambda x,y: int(x + y) - int(y + x)), reverse=True)
        return ''.join(nums) if nums[0] != '0' else '0'
