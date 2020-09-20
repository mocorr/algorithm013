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
#  👍 253 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

    def isAnagram3(self, s: str, t: str) -> bool:
        dic_s, dic_t = dict(), dict()
        for ch in s:
            dic_s[ch] = dic_s.get(ch, 0) + 1
        for ch in t:
            dic_t[ch] = dic_t.get(ch, 0) + 1
        return dic_s == dic_t

    def isAnagram4(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = dict()
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            dic[ch] = dic.get(ch, 0) - 1
            if dic[ch] < 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
