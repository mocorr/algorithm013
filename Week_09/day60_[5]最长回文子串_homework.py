# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2722 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        1 奇数 i = j
        2 偶数 i - j = 1 and s[i] = s[j]
        3 s[i] = s[j] dp[j + 1][i - 1] = 1
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = 0
        tmp = ''
        for i in range(n):
            for j in range(i + 1):
                if s[j] == s[i] and (i - j <= 1 or dp[j + 1][i - 1] >= 1):
                    dp[j][i] = 1 * (i - j + 1)
                    if dp[j][i] > max_len:
                        max_len = dp[j][i]
                        tmp = s[j:i + 1]
        return tmp

# leetcode submit region end(Prohibit modification and deletion)
