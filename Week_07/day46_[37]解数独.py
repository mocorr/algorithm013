# 编写一个程序，通过已填充的空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  Note: 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 524 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    注意不能填入0
    """
    def solveSudoku(self, board):
        """
        时间复杂度O(n^3), 其中n = 9
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    val = int(board[x][y])
                    rows[x].add(val)
                    cols[y].add(val)
                    boxs[x // 3 * 3 + y // 3].add(val)

        def _dfs(i, j):
            if i == 8 and j == 9:  # 已全部解出
                return True
            if j == 9:  # 换行
                return _dfs(i + 1, 0)
            if board[i][j] != '.':  # 跳过
                return _dfs(i, j + 1)

            for k in range(1, 10):
                if k in rows[i] or k in cols[j] or k in boxs[i // 3 * 3 + j // 3]:
                    continue
                board[i][j] = str(k)
                rows[i].add(k)
                cols[j].add(k)
                boxs[i // 3 * 3 + j // 3].add(k)

                if _dfs(i, j + 1):  # 如果解出，不再恢复当前层
                    return True

                board[i][j] = '.'
                rows[i].remove(k)
                cols[j].remove(k)
                boxs[i // 3 * 3 + j // 3].remove(k)
            return False

        _dfs(0, 0)



# leetcode submit region end(Prohibit modification and deletion)

