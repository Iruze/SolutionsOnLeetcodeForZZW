/**
 * 845. 数组中的最长山脉 LeetCode Medium
 *
 * @param A
 * @return
 */
// ref: 
// https://leetcode-cn.com/problems/longest-mountain-in-array/solution/leetcode-shan-feng-shu-zu-san-ti-by-a-fei-8/
public int longestMountain(int[] A) {
    if (A == null || A.length < 3) {
        return 0;
    }
    int res = 0;
    for (int i = 1; i < A.length - 1; i++) {
        //find the maxium number [peak mountain]
        if (A[i] > A[i - 1] && A[i] > A[i + 1]) {
            //get the left pointer and right pointer, expand from the center ,get the maximum boundary
            int l = i - 1;
            int r = i + 1;
            while (l > 0 && A[l - 1] < A[l]) {
                l--;
            }
            while (r < A.length - 1 && A[r] > A[r + 1]) {
                r++;
            }
            //record the maximum len
            res = Math.max(res, r - l + 1);
        }
    }
    return res;
}
