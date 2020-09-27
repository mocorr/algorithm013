# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  说明：m 和 n 的值均不超过 100。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
#  Related Topics 数组 动态规划 
#  👍 413 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (w + 1) for _ in range(h + 1)]
        for i in range(h - 1, -1, -1):
            for j in range(w - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == h - 1 and j == w - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]
# leetcode submit region end(Prohibit modification and deletion)
