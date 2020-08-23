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
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(y, x):
            for a, b in [(y, x + 1), (y, x - 1), (y - 1, x), (y + 1, x)]:
                if 0 <= a < h and 0 <= b < w and grid[a][b] == '1':
                    grid[a][b] = 0
                    helper(a, b)

        if not grid:
            return 0
        count = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(w):
            for j in range(h):
                if grid[j][i] == '1':
                    count += 1
                    helper(j, i)
        return count





# leetcode submit region end(Prohibit modification and deletion)
