# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。 
# 
#  示例: 
# 
#  Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true 
# 
#  说明: 
# 
#  
#  你可以假设所有的输入都是由小写字母 a-z 构成的。 
#  保证所有输入均为非空字符串。 
#  
#  Related Topics 设计 字典树 
#  👍 399 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    """
    insert、search、startsWith的核心操作其实都一样：
    如果当前字母存在，就继续找，如果不存在就插入/结束。
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

    # def print_root(self):
    #     print(self.root)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert('apple')
# obj.print_root()
# param_2 = obj.search('apple')
# param_3 = obj.search('app')
# param_4 = obj.startsWith('app')
# obj.insert('app')
# obj.print_root()
# param_5 = obj.search('app')
# obj.insert('appqwe')
# obj.print_root()
# print(param_2, param_3, param_4, param_5)
# leetcode submit region end(Prohibit modification and deletion)
