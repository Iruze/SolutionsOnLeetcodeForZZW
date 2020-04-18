class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # 每个字符串26字母映射作为哈希的key
            ans[tuple(count)].append(s)
        return [*ans.values()]
