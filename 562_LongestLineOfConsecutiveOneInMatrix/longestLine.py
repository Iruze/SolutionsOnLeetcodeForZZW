# solution1:
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        res = 0
        rows, cols = len(M), len(M[0])
        dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1
                    dp[i][j][2] = dp[i - 1][j - 1][2] + 1 if i > 0 and j > 0 else 1
                    dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if i > 0 and j < cols - 1 else 1
                    res = max(res, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return res
        
# solution2:
public class Solution {
    public int longestLine(int[][] M) {
        if (M.length == 0)
            return 0;
        int ones = 0;
        int[][] dp = new int[M[0].length][4];
        for (int i = 0; i < M.length; i++) {
            int old = 0;
            for (int j = 0; j < M[0].length; j++) {
                if (M[i][j] == 1) {
                    dp[j][0] = j > 0 ? dp[j - 1][0] + 1 : 1;
                    dp[j][1] = i > 0 ? dp[j][1] + 1 : 1;
                    int prev = dp[j][2];
                    dp[j][2] = (i > 0 && j > 0) ? old + 1 : 1;
                    old = prev;
                    dp[j][3] = (i > 0 && j < M[0].length - 1) ? dp[j + 1][3] + 1 : 1;
                    ones = Math.max(ones, Math.max(Math.max(dp[j][0], dp[j][1]), Math.max(dp[j][2], dp[j][3])));
                } else {
                    old = dp[j][2];
                    dp[j][0] = dp[j][1] = dp[j][2] = dp[j][3] = 0;
                }
            }
        }
        return ones;
    }
}
