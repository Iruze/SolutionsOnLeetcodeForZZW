class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 前缀和
        pre = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            pre[i + 1] = pre[i] ^ arr[i]
        
        ans = []
        for x, y in queries:
            ans.append(pre[y + 1] ^ pre[x])
        
        return ans
