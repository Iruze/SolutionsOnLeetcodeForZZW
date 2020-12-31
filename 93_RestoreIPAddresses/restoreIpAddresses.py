# dfs
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) < 4: 
            return []
        def helper(s, cur=[]):
            if len(cur) + len(s) < 4:
                return
            # base case: 已经有了3个数，s必须作为最后一个数
            if len(cur) == 3:
                if s == '0' or s[0] != '0' and 0 < int(s) < 256:
                    ans.append('.'.join(cur+[s]))
                return
            # 在s的头部找出当前的数，最长为3位
            for i in range(min(3, len(s))):
                # s[0]是'0'，只有能作一个数，否则就是前导0了
                if s[0] == '0':
                    helper(s[1:], cur + ['0'])
                    break
                s1 = s[:i+1]
                # 符合ip要求，加入cur
                if 0 < int(s1) < 256:
                    helper(s[i+1:], cur + [s1])
        helper(s)
        return ans
        
# 回溯- 2019-12-03
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if s and len(s) <= 12 and 0 <= len(s):
            self.__dfs(s, '', res, 1)
        return res
    
    
    def __dfs(self, s, pre='', res=[], depth=1):
        if depth == 4:
            if self.checkIpValid(s):
                res.append(pre + s)
            return
        for i in [0, 1, 2]:
            d = s[0: i + 1]
            s = s[i+1 :]
            if s and d and self.checkIpValid(d):
                tmp = pre
                pre += d + '.'
                self.__dfs(s, pre, res, depth + 1)
                pre = tmp
            s = d + s
            
    
    def checkIpValid(self, s):
        Valid = True
        if 255 < int(s) or int(s) < 0:
            Valid = False
        if s[0] == '0' and len(s) > 1:
            Valid = False
        return Valid
