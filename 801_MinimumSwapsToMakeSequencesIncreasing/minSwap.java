// 参考： https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing/solution/801-fen-bie-tao-lun-huan-he-bu-huan-fen-bie-bao-cu/


class Solution {
    public int minSwap(int[] A, int[] B) {
        int n = A.length;
        int[][] dp = new int[n][2];
        dp[0][0] = 0;
        dp[0][1] = 1;
        for(int i = 1; i < n; ++i) {
            //1. 已经各自有序
            //2. 存在交叉
            //3. 既有序，也交叉
            if(A[i - 1] < A[i] && B[i - 1] < B[i]) {// 各自有序
                if(A[i - 1] < B[i] && B[i - 1] < A[i]) {// 且存在交叉
                    dp[i][0] = Math.min(dp[i - 1][0], dp[i - 1][1]);
                    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][1]) + 1;
                } else {// 有序但不存在交叉
                    dp[i][0] = dp[i - 1][0];//不交换，再上一轮不交换的基础上，不变。
                    dp[i][1] = dp[i - 1][1] + 1;// 由于不存在交叉，所以如果要交换的话，得在上一轮交换的基础上，本轮再次交换
                }
            } else {//无序，则必然存在交叉
                dp[i][0] = dp[i - 1][1];// 由于必须交叉，所以如果要不换的话，必须在上一轮交换的基础上，本轮才可以不交换
                dp[i][1] = dp[i - 1][0] + 1;// 同上，必须在上一轮不交换的基础上，本轮交换
            }
        }

        return Math.min(dp[n - 1][0], dp[n - 1][1]);
    }
}
