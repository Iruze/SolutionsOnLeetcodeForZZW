# 回溯法
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.ans = 0
        all_set = set(range(1, 10))
        def backtrack(cur_set, pre):
            if len(cur_set) >= m:
                self.ans += 1
                if len(cur_set) == n:
                    return
            for num in all_set - cur_set:
                diff = abs(num - pre)
                if diff == 2 and min(pre, num) in {1, 4, 7} and (num + pre) // 2 not in cur_set: continue
                if diff == 4 and min(pre, num) == 3 and 5 not in cur_set: continue
                if diff == 6 and (num + pre) // 2 not in cur_set: continue
                if diff == 8 and 5 not in cur_set: continue
                backtrack(cur_set | {num}, num)
        for i in range(1, 10):
            backtrack({i}, i)
        return self.ans
        
