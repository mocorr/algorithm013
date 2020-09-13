# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  示例: 
# 
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步
# ，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法 
#  👍 504 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = []
        self.cols = []
        self.diffs = []  # 行列序号之差若相同，在同一条\上
        self.sums = []  # 行列序号之和若相同，在同一条/上

    def solveNQueens1(self, n: int) -> List[List[str]]:
        """
        回溯法
        """
        self.dfs(0, n, [])
        return self._generate()

    def dfs(self, row, n, tmp):
        # recursion terminator
        if row == n:
			# 这里绝不能直接append(self.cols), 可以用一个当前层变量存储 或 加上.copy()
			# list中存放的是self.cols的地址, 修改self.cols也会改变self.res
            self.res.append(tmp)  
            return

        # try all options
        for col in range(n):
            if col in self.cols or col - row in self.diffs or col + row in self.sums:
                continue

            # process logic in current layer
            self.cols.append(col)
            self.diffs.append(col - row)
            self.sums.append(col + row)

            # drill down
            self.dfs(row + 1, n, tmp + [col])

            # revert
            self.cols.pop()
            self.diffs.pop()
            self.sums.pop()

    def _generate(self):
        return [['.' * row + 'Q' + '.' * (len(sol) - 1 - row) for row in sol] for sol in self.res]

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        简化版本
        """

        def dfs(row, cols, diffs, sums):
            if row == n:
                res.append(cols)
                return
            for col in range(n):
                if col in cols or col - row in diffs or col + row in sums:
                    continue
                dfs(row + 1, cols + [col], diffs + [col - row], sums + [col + row])
                # 这里不需要恢复当前层，因为cols, diffs, sums是层层传递的，不会对其他分支造成影响（也没法恢复

        res = []
        dfs(0, [], [], [])
        return [['.' * row + 'Q' + '.' * (len(sol) - 1 - row) for row in sol] for sol in res]

# leetcode submit region end(Prohibit modification and deletion)
