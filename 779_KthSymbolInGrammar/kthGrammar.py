class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1: return 0
        if K <= 2 ** (N - 2):
            return self.kthGrammar(N - 1, K)
        return self.kthGrammar(N - 1, K - 2 ** (N - 2)) ^ 1
