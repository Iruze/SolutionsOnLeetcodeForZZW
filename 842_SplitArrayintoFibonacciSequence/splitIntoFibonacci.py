class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        def dfs(S, cur=[]):
            # 前几步剪枝操作， 提前将不满足条件的分支剔除
            if not cur and len(S) < 3: 
                return False
            if len(cur) == 1 and len(str(cur[0])) + 1 > len(S):
                return False
            if len(cur) >= 2 and not S.startswith(str(sum(cur[-2:]))):
                return False
            # 找到了一个斐波拉契拆分，即可返回，无需再继续下去
            if int(S) < 2 ** 31 and S == str(sum(cur[-2:])):
                self.ans = cur[:] + [int(S)]
                return True
            for i in range(1, len(S) // 2 + 1):
                # 存在拆分为0的特殊处理
                if S[0] == '0':
                    if dfs(S[1:], cur + [0]): return True
                    else: break
                # 拆分的数超出范围，不满足，退出
                if int(S[:i]) >= 2 ** 31: break
                if (len(cur) < 2 or S[:i] == str(sum(cur[-2:]))) and dfs(S[i:], cur + [int(S[:i])]):
                    return True
            # 找不到合理的拆分，返回false
            return False
        
        self.ans = []
        dfs(S)
        return self.ans
