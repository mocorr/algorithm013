# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回 n 皇后不同的解决方案的数量。 
# 
#  示例: 
# 
#  输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N
# -1 步，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法 
#  👍 147 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens1(self, n: int) -> int:
        def _dfs(i, cols, diffs, sums):
            if i == n:
                count[0] += 1
                return
            for j in range(n):
                if j in cols or i - j in diffs or i + j in sums:
                    continue
                _dfs(i + 1, cols + [j], diffs + [i - j], sums + [i + j])

        count = [0]
        _dfs(0, [], [], [])
        return count[0]

    def totalNQueens(self, n):
        def _dfs(i, cols, diffs, sums):
            if i == n:
                count[0] += 1
                return
            bits = (~(cols | diffs | sums)) & size  # 得到当前所有的空位
            while bits:
                p = bits & - bits  # 取到最低位的1
                bits = bits & (bits - 1)  # 消掉最低位的1
                _dfs(i + 1, cols | p, (diffs | p) << 1, (sums | p) >> 1)

        count = [0]
        size = (1 << n) - 1
        _dfs(0, 0, 0, 0)

        return count[0]
# leetcode submit region end(Prohibit modification and deletion)
