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
        def _dfs(x, y):
            for x_next, y_next in ((x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)):
                if 0 <= x_next < h and 0 <= y_next < w and grid[x_next][y_next] == '1':
                    grid[x_next][y_next] = '0'
                    _dfs(x_next, y_next)

        if not grid:
            return 0
        cnt = 0
        h, w = len(grid), len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    cnt += 1
                    _dfs(i, j)
        return cnt

    def numIslandsP(self, grid: List[List[str]]) -> int:
        """
        并查集法
        """
        def _parent(x):
            root = x
            while p[root] != root:
                root = p[root]
            while p[x] != x:
                x, p[x] = p[x], root
            return root

        def _union(x, y):
            p[_parent(x)] = _parent(y)

        if not grid:
            return 0
        h, w = len(grid), len(grid[0])
        p = [i for i in range(h * w)]

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    for i_next, j_next in ((i, j + 1), (i + 1, j)):  # 只需要走正向
                        if 0 <= i_next < h and 0 <= j_next < w and grid[i_next][j_next] == "1":
                            _union(i * w + j, i_next * w + j_next)

        res = set()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    res.add(_parent(i * w + j))

        return len(res)

# leetcode submit region end(Prohibit modification and deletion)
