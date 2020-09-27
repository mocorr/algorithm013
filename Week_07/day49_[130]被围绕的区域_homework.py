# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。 
# 
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。 
# 
#  示例: 
# 
#  X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  运行你的函数后，矩阵变为： 
# 
#  X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  解释: 
# 
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 364 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveDFS(self, board: List[List[str]]) -> None:
        """
        DFS法 思路：染一个特殊的颜色
        """
        def _dfs(row, col):
            if board[row][col] == "O":
                board[row][col] = "F"
                for x, y in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if 0 <= x < h and 0 <= y < w:
                        _dfs(x, y)

        if not board:
            return
        h, w = len(board), len(board[0])

        for i in range(h):
            _dfs(i, 0)
            _dfs(i, w - 1)
        for j in range(w):
            _dfs(0, j)
            _dfs(h - 1, j)

        for i in range(h):
            for j in range(w):
                if board[i][j] == "F":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def solveP(self, board: List[List[str]]) -> None:
        """
        并查集法 思路：union with dummy（比如四顶点）
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

        if not board:
            return
        h, w = len(board), len(board[0])
        p = [i for i in range(h * w)]

        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                        _union(i * w + j, 0)
                    for tmp_i, tmp_j in ((i + 1, j), (i, j + 1)):  # 只要是“O”就去扩散
                        if 0 <= tmp_i < h and 0 <= tmp_j < w and board[tmp_i][tmp_j] == "O":
                            _union(tmp_i * w + tmp_j, i * w + j)

        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    if _parent(i * w + j) != _parent(0):
                        board[i][j] = "X"
# leetcode submit region end(Prohibit modification and deletion)
