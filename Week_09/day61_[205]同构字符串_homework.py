# 给定两个字符串 s 和 t，判断它们是否是同构的。 
# 
#  如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。 
# 
#  所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。 
# 
#  示例 1: 
# 
#  输入: s = "egg", t = "add"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "foo", t = "bar"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: s = "paper", t = "title"
# 输出: true 
# 
#  说明: 
# 你可以假设 s 和 t 具有相同的长度。 
#  Related Topics 哈希表 
#  👍 242 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        时间复杂度O(n)
        思路：将s与t的元素一一映射，若key或val已经存在却不对应则非同构
        """
        dic = dict()
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
                dic[s[i]] = t[i]
        return True

    def isIsomorphic1(self, s: str, t: str) -> bool:
        """
        时间复杂度O(n^2) 类似并查集find_parent的思路
        """
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
