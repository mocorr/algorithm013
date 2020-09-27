# 给定一个字符串，逐个翻转字符串中的每个单词。 
# 
#  
# 
#  示例 1： 
# 
#  输入: "the sky is blue"
# 输出: "blue is sky the"
#  
# 
#  示例 2： 
# 
#  输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#  
# 
#  示例 3： 
# 
#  输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  
# 
#  
# 
#  说明： 
# 
#  
#  无空格字符构成一个单词。 
#  输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。 
#  如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。 
#  
# 
#  
# 
#  进阶： 
# 
#  请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。 
#  Related Topics 字符串 
#  👍 225 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        手写api
        """
        def trim_spaces():
            left, right = 0, len(s) - 1
            # 去掉字符串头尾的空白字符
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1
            # 将字符串间多余的空白字符去除
            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output[-1] != ' ':
                    output.append(s[left])
                left += 1
            return output

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

        s = trim_spaces()
        reverse(0, len(s) - 1)
        print(s)
        reverse_each_word()
        return ''.join(s)

    def reverseWords1(self, s: str) -> str:
        """
        将s按空格分割 --> (使用.split(' ')还需滤去list中的空字符串) --> 翻转list --> 转回string
        """
        return ' '.join(s.split()[::-1])

# leetcode submit region end(Prohibit modification and deletion)
