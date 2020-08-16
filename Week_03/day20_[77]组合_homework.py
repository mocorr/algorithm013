# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 328 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combineBad(self, n: int, k: int) -> List[List[int]]:
        """
        生成子集再判断长度
        """
        res = [[]]
        for i in range(1, n + 1):
            res.extend([r + [i] for r in res if len(r) < k])
        return [r for r in res if len(r) == k]

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        递归法(回溯)
        """
        def helper(index, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(index, n+1):
                helper(i + 1, tmp + [i])

        res = []
        helper(1, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
