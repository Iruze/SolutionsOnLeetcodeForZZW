# 栈模拟，行星碰撞的逻辑

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            boom = False
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] >= -a:
                    # 行星一样大， 同时爆炸
                    if stack[-1] == -a: stack.pop()
                    boom = True
                    break
                else:
                    # 已入栈的小行星爆炸
                    stack.pop()
            # 当前行星没有被爆炸，可以入栈
            if not boom:
                stack.append(a)
        return stack
