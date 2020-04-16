class Solution {
    public int countCornerRectangles(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int ans = 0;

        # 固定上下两条边r1, r2
        for(int r1 = 0; r1 < rows - 1; ++r1) {
            for(int r2 = r1 + 1; r2 < rows; ++r2) {
                int count = 0;
                # 对r1, r2两条边逐列扫描
                for(int c = 0; c < cols; ++c) {
                    if(grid[r1][c] == 1 && grid[r2][c] == 1) {
                        count++;
                    }
                }

                # count条符合的列，则选出两条：Cn2组合
                ans += count * (count - 1) / 2;
            }
        }

        return ans;
    }
}
