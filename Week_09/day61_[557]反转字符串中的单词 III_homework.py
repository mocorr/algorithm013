# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。 
# 
#  
# 
#  示例： 
# 
#  输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#  
# 
#  
# 
#  提示： 
# 
#  
#  在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。 
#  
#  Related Topics 字符串 
#  👍 245 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords1(self, s: str) -> str:
        """
        手写api
        """

        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        def reverse_each_word():
            n = len(s)
            start = end = 0
            while start < n:
                # 找到每个单词的末尾
                while end < n and s[end] != ' ':
                    end += 1
                # 翻转当前单词
                reverse(start, end - 1)
                # 更新start，去找下一个单词
                start = end + 1
                end += 1

        s = list(s)
        reverse_each_word()
        return ''.join(s)

    def reverseWords(self, s: str) -> str:
        """
        将s按空格分割 --> 按单词翻转 --> 转回string
        """
        return ' '.join(word[::-1] for word in s.split())
# leetcode submit region end(Prohibit modification and deletion)
