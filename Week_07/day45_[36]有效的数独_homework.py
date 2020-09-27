# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  
# 
#  上图是一个部分填充的有效的数独。 
# 
#  数独部分空格内已填入了数字，空白格用 '.' 表示。 
# 
#  示例 1: 
# 
#  输入:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
#      但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。 
# 
#  说明: 
# 
#  
#  一个有效的数独（部分已被填充）不一定是可解的。 
#  只需要根据以上规则，验证已经填入的数字是否有效即可。 
#  给定数独序列只包含数字 1-9 和字符 '.' 。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 
#  👍 413 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = board[i][j]
                    if val in row[i] or val in col[j] or val in box[i // 3 * 3 + j // 3]:
                        return False
                    row[i][val] = 1
                    col[j][val] = 1
                    box[i // 3 * 3 + j // 3][val] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if rows[i][val - 1] or cols[j][val - 1] or boxes[i // 3 * 3 + j // 3][val - 1]:
                        return False
                    rows[i][val - 1] = 1
                    cols[j][val - 1] = 1
                    boxes[i // 3 * 3 + j // 3][val - 1] = 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
