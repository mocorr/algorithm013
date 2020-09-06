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
#  👍 649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum1(self, grid: List[List[int]]) -> int:
        """
        递归超时写法1（回溯写法） 时间复杂度O(2^(m+n))
        """

        def _helper(row, col, tmp):
            tmp += grid[row][col]
            if row == m - 1 and col == n - 1:
                res[0] = min(res[0], tmp)
                return
            if row < m - 1:
                _helper(row + 1, col, tmp)
            if col < n - 1:
                _helper(row, col + 1, tmp)

        m = len(grid)
        n = len(grid[0])
        res = [float(inf)]
        _helper(0, 0, 0)
        return int(res[0])

    def minPathSum2(self, grid: List[List[int]]) -> int:
        """
        递归超时写法2
        """

        def _helper(row, col):
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            elif row == m - 1:
                return grid[row][col] + _helper(row, col + 1)
            elif col == n - 1:
                return grid[row][col] + _helper(row + 1, col)
            return grid[row][col] + min(_helper(row, col + 1), _helper(row + 1, col))

        m = len(grid)
        n = len(grid[0])
        return _helper(0, 0)

    def minPathSum3(self, grid: List[List[int]]) -> int:
        """
        递归超时写法2 的记忆化
        """
        def _helper(row, col):
            if (row, col) in dic:
                return dic[(row, col)]
            if row == height - 1 and col == width - 1:
                dic[(row, col)] = grid[row][col]
            elif row == height - 1:
                dic[(row, col)] = _helper(row, col + 1) + grid[row][col]
            elif col == width - 1:
                dic[(row, col)] = _helper(row + 1, col) + grid[row][col]
            else:
                dic[(row, col)] = min(_helper(row, col + 1), _helper(row + 1, col)) + grid[row][col]
            return dic[(row, col)]

        height = len(grid)
        width = len(grid[0])
        dic = {}
        return _helper(0, 0)

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp 时间复杂度O(mn)
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                elif i == m - 1:
                    grid[i][j] += grid[i][j + 1]
                elif j == n - 1:
                    grid[i][j] += grid[i + 1][j]
                else:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]
# leetcode submit region end(Prohibit modification and deletion)
