""" bfs 广度优先搜索： 
挨个删除'()'，视为一层，下次再次遍历删除'()'，得到新的一层
逐层遍历，得到最小删除步数
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 判断合法括号的函数
        def isvalid(s):
            cnt = 0
            for c in s:
                if c == '(': cnt += 1
                elif c == ')': cnt -= 1
                if cnt < 0: return False
            return cnt == 0
        
        # cur, nxt分别是当前层和下一层
        cur, nxt = {s}, set()
        while True:
            ans = list(filter(isvalid, cur))
            # 筛选出来了，说明合法括号产生了，注意['']也是True
            if ans: return ans
            for item in cur:
                for i, c in enumerate(item):
                    # 挨个删除'()'
                    if c in '()':
                        nxt.add(item[:i] + item[i+1:])
            cur, nxt = nxt, set()
