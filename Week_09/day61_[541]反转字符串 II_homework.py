# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例: 
# 
#  输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#  
# 
#  
# 
#  提示： 
# 
#  
#  该字符串只包含小写英文字母。 
#  给定字符串的长度和 k 在 [1, 10000] 范围内。 
#  
#  Related Topics 字符串 
#  👍 91 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    python字符串是一种不可变对象(immutabel object)
    不能直接对某一位进行赋值，只读不写。转list
    """

    def reverseStr(self, s: str, k: int) -> str:
        """
        直接调用[::-1]
        """
        s = list(s)
        for left in range(0, len(s), 2 * k):
            s[left:left + k] = s[left:left + k][::-1]
        return ''.join(s)

    def reverseStr1(self, s: str, k: int) -> str:
        """
        手写reverse
        """

        def reverse(i, j):
            j = min(j, len(s) - 1)
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        s = list(s)
        for left in range(0, len(s), 2 * k):
            reverse(left, left + k - 1)
        return ''.join(s)
# leetcode submit region end(Prohibit modification and deletion)
