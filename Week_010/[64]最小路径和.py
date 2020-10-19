# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  示例: 
# 
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#  
#  Related Topics 数组 动态规划 
#  👍 689 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum1(self, grid: List[List[int]]) -> int:
        """
        DP二维 未padding
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = dp[i + 1][n - 1] + grid[i][n - 1]
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = dp[m - 1][j + 1] + grid[m - 1][j]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return dp[0][0]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        """
        DP二维 padding inf
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[float(inf)] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return dp[0][0]

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        DP一维 空间优化
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = grid[-1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                elif i == m - 1:
                    dp[j] += dp[j + 1]
                elif j == n - 1:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j + 1]) + grid[i][j]
        return dp[0]
# leetcode submit region end(Prohibit modification and deletion)
