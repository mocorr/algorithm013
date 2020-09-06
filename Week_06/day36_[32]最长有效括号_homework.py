# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 940 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        思路：左括号index入栈，右括号对应的左括号index出栈并计算长度
        右括号index当且仅当栈中无左括号时入栈，即栈为空或者栈顶为)index
        不匹配的)之所以入栈而非直接continue是为了计算长度
        """
        if not s:
            return 0
        res = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or not stack or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
                res = max(res, i - stack[-1] if stack else i + 1)
        return res

# leetcode submit region end(Prohibit modification and deletion)
