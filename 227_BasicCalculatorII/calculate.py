# 参考了： https://leetcode-cn.com/problems/basic-calculator-ii/solution/pythonde-dan-zhan-jie-fa-by-a-bai-152/

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = list()
        # 前一个符号操作
        front = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            # 遇到第二个符号或者最后一个字符时，清算
            if c in '+-*/' or i == len(s) - 1:
                if front == '+':
                    stack.append(num)
                if front == '-':
                    stack.append(-num)
                if front == '*':
                    stack[-1] = stack[-1] * num
                if front == '/':
                    stack[-1] = int(stack[-1] / num)
                front = c 
                num = 0
        return sum(stack)
