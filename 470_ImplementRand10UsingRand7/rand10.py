# 拒接采样算法

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) * 7 + rand7()
        # num > 30, 20, 10都行，不过概率低，时间效率差
        while num > 40:
            num = (rand7() - 1) * 7 + rand7()
        return (num - 1) % 10 + 1

"""
# 扩展：rand10 -> rand7()

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = rand10()
        while num > 7:
            num = rand10()
        return num
        
"""
