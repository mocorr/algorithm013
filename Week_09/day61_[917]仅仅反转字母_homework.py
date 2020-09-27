# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入："ab-cd"
# 输出："dc-ba"
#  
# 
#  示例 2： 
# 
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#  
# 
#  示例 3： 
# 
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 100 
#  33 <= S[i].ASCIIcode <= 122 
#  S 中不包含 \ or " 
#  
#  Related Topics 字符串 
#  👍 61 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        """
        c.isalpha()比 c in string.ascii_letters 高效很多
        """

        def reverse(left, right):
            while left < right:
                while left < right and not s[left].isalpha():
                    left += 1
                while left < right and not s[right].isalpha():
                    right -= 1
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        s = list(S)
        reverse(0, len(s) - 1)
        return ''.join(s)

# leetcode submit region end(Prohibit modification and deletion)
