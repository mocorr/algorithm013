# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索 
#  👍 409 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def ladderLengthDfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        单向DFS set比list快（in/not in的查询时间）
        """
        begin_set = {beginWord}
        word_set = set(wordList)
        dis = 1
        if endWord not in word_set:
            return 0
        while begin_set:
            dis += 1
            next_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    ch = word[i]
                    for j in range(26):
                        new_ch = chr(ord('a') + j)
                        if new_ch != ch:
                            new_word = word[:i] + new_ch + word[i + 1:]
                            if new_word == endWord:
                                return dis
                            if new_word in word_set:
                                next_set.add(new_word)
                                word_set.remove(new_word)  # 注意要移除已尝试词
            begin_set = next_set
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        双向DFS
        """
        begin_set = {beginWord}
        end_set = {endWord}
        word_set = set(wordList)
        dis = 1
        if endWord not in word_set:
            return 0
        while begin_set:
            dis += 1
            next_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    ch = word[i]
                    for j in range(26):
                        new_ch = chr(ord('a') + j)
                        if new_ch != ch:
                            new_word = word[:i] + new_ch + word[i + 1:]
                            if new_word in end_set:
                                return dis
                            if new_word in word_set:
                                next_set.add(new_word)
                                word_set.remove(new_word)  # 注意要移除已尝试词
            begin_set = next_set
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
        return 0
# leetcode submit region end(Prohibit modification and deletion)
