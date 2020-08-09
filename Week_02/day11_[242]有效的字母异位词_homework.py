# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 排序 哈希表 
#  👍 223 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        时间复杂度O(n) 比较的时间复杂度是? 空间复杂度O(n)
        """
        return self.countCh(s) == self.countCh(t)

    def countCh(self, word):
        ch_dict = {}
        for ch in word:
            if ch in ch_dict:
                ch_dict[ch] += 1
            else:
                ch_dict[ch] = 1
        return ch_dict
# leetcode submit region end(Prohibit modification and deletion)
