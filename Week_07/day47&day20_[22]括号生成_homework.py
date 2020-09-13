# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1222 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesisBad(self, n: int) -> List[str]:
        """
        暴力递归最后剪枝 时间复杂度O(n * 2^n) 空间复杂度O(n)?
        """

        def valid(s):
            """
            验证括号的有效性 时间复杂度O(n) 空间复杂度O(n)
            """
            stack = []
            for ch in s:
                if ch == '(':
                    stack.append(ch)
                else:
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0

        def helper(level, tmp):
            if level >= 2 * n:
                if valid(tmp):
                    res.append(tmp)
                return
            helper(level + 1, tmp + '(')
            helper(level + 1, tmp + ')')

        res = []
        helper(0, '')
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        """
        递归法 时间复杂度O(2^n) 空间复杂度O(n)?
        """

        def helper(left, right, tmp):
            if left == n and right == n:
                res.append(tmp)
                return
            if left <= n:
                helper(left + 1, right, tmp + '(')
            if right < left:
                helper(left, right + 1, tmp + ')')

        res = []
        helper(0, 0, '')
        return res
# leetcode submit region end(Prohibit modification and deletion)
