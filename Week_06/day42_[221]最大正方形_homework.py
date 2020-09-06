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
#  👍 534 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        时间复杂度O(mn) 空间复杂度O(mn)
        关键：由面积问题转为边长问题
        """
        if not matrix:
            return 0
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0] * width for _ in range(height)]
        max_side = 0
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
# leetcode submit region end(Prohibit modification and deletion)
