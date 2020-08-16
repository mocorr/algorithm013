# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 420 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        将单词的排序字符串作为键，单词本身作为值
        时间复杂度：O(NKlogK),N是strs的长度,K是strs中字符串的最大长度
        空间复杂度：O(NK)
        """
        dic = {}
        for word in strs:
            word_sorted = tuple(sorted(word))  # tuple可以作为字典的key，list不可以
            # if word_sorted in dic:
            #     dic[word_sorted].append(word)
            # else:
            #     dic[word_sorted] = [word]
            dic[word_sorted] = dic.get(word_sorted, []) + [word]
        # return [dic[k] for k in dic]
        return dic.values()
# leetcode submit region end(Prohibit modification and deletion)
