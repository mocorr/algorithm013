# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。 
# 
#  示例: 
# 
#  输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4 
#  Related Topics 动态规划 
#  👍 587 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquareDp(self, matrix: List[List[str]]) -> int:
        """
        二维DP
        """
        if not matrix:
            return 0
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        dp = [[0] * n for _ in range(m)]
        dp_max = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    dp_max = max(dp_max, dp[i][j])
        return dp_max * dp_max

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        一维DP 空间优化 滚动数组
        """
        if not matrix:
            return 0
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        dp = [0] * n
        dp_max = 0
        for i in range(1, m):
            tmp = [0] * n
            for j in range(1, n):
                if matrix[i - 1][j - 1] == "1":
                    tmp[j] = min(dp[j], tmp[j - 1], dp[j - 1]) + 1
                    dp_max = max(dp_max, tmp[j])
            dp = tmp
        return dp_max * dp_max
# leetcode submit region end(Prohibit modification and deletion)
