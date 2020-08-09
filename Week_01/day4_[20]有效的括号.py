# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true 
#  Related Topics 栈 字符串 
#  👍 1728 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        """
        利用栈进行比对 时间复杂o(n)
        """
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not ((top == '(' and i == ')') or (top == '[' and i == ']') or (top == '{' and i == '}')):
                    return False
        return len(stack) == 0

    def isValidDic(self, s: str) -> bool:
        """
        同上 利用dict使代码更美观更具可拓展性
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif not stack or dic[stack.pop()] != i:
                return False
        return len(stack) == 0

# leetcode submit region end(Prohibit modification and deletion)
