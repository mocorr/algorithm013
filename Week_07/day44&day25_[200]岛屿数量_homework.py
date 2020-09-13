# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 720 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        """
        DFS法
        """
        def _helper(row, col):
            for x, y in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                    grid[x][y] = "0"
                    _helper(x, y)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    _helper(i, j)
        return cnt

    def numIslandsP(self, grid: List[List[str]]) -> int:
        """
        并查集法
        """
        def _union(x, y):
            p[_parent(x)] = _parent(y)

        def _parent(x):
            root = x
            while p[root] != root:
                root = p[root]
            while p[x] != x:
                x, p[x] = p[x], root
            return root

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        p = [i for i in range(rows * cols)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    for tmp_i, tmp_j in ((i + 1, j), (i, j + 1)):
                        if 0 <= tmp_i < rows and 0 <= tmp_j < cols and grid[tmp_i][tmp_j] == "1":
                            _union(tmp_i * cols + tmp_j, i * cols + j)

        res = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res.add(_parent(i * cols + j))
        return len(res)

# leetcode submit region end(Prohibit modification and deletion)
