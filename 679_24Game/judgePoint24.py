from operator import add, sub, mul, truediv


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        """
        无非是4个数中间夹杂着4种符号的排列；
        1. 从4个数中取2个运算：A42 = 12，得到1个数
        2. 从剩下的3个数取2个来运算：A32 = 6，得到1个数
        3. 剩下2个数，A21 = 2
        从1-3， 每一步有4种运算符号，一共= 12*6*2*(4**3) = 9216种情况
        """
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                # 从4个数中取2个不同的数
                if i != j:
                    # 剩下的2个数
                    rest = [nums[k] for k in range(len(nums)) if i != k != j]
                    # 开始运算
                    for op in (add, sub, mul, truediv):
                        # add和mul位置可交换有两种情况，过滤掉其中一种
                        if (op is add or op is mul) and i > j: continue
                        # 当运算符为/时， 除数不能是0
                        if not (op is truediv and nums[j] == 0):
                            # 4个数其中2个做了运算，剩下3个，递归求解
                            rest.append(op(nums[i], nums[j]))
                            if self.judgePoint24(rest): return True 
                            rest.pop()
        return False
        
