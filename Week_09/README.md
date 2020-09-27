# Week9学习笔记

---

## 1. 知识点

本周的知识点和前面的课程都大同小异（并且今天补班&人不舒服&精神恍惚）就不整理知识点了

## 2.不同路径Ⅱ

和不同路径Ⅰ几乎一模一样，注意padding的技巧即可。

```python
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
```