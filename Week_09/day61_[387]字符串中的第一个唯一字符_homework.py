# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串 
#  👍 269 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar1(self, s: str) -> int:
        """
        手动计数
        """
        dic = dict()
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
            # dic[s[i]] = dic.get(s[i], 0) + 1  # 更慢
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1

    def firstUniqChar(self, s: str) -> int:
        """
        直接调用counter
        """
        count = collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
