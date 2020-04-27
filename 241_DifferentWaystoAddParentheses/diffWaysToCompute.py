class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def helper(l, r, op):
            if op == '+': return l + r
            if op == '-': return l - r 
            if op == '*': return l * r

        if input.isdigit():
            return [int(input)]
        ans = []
        for i, op in enumerate(input):
            if op in {'+', '-', '*'}:
                # 分治思想
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                ans += [helper(l, r, op) for l in left for r in right]
        return ans
