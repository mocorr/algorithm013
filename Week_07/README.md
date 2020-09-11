# 学习笔记

[TOC]



## Trie
### 基本定义：

字典树，又称前缀树(Prefix Tree)、单词查找树、键树。
工程中多为有序树、多叉树结构，其键值多为**字符串**。
主要用于保存关连数组，**键并不直接保存在节点中，而是由节点所在树中的位置决定。**

一个节点的所有子孙都有相同的前缀，也就是这个节点对应的字符串，而根节点对应空字符串。一般情况下，不是所有的节点都有对应的值，只有叶子节点和部分内部节点所对应的键才有相关的值。

优点：最大限度的减少无效的字符串比较，查询效率比Hash表高

经典应用：统计、排序大量字符串。搜索引擎文本词频统计等

### 基本性质：

- 节点本身不存完整单词
- 从根节点到某一结点，路径上经过的字符连起来，为该节点对应的字符串
- 每个节点所有的子节点路径代表的字符都不相同

### 核心思想：

Trie树的核心思想是空间换时间

利用字符串的公共前缀来降低查询的时间开销，以达到提高效率的目的

### Trie树实现:

~~~python
class Trie:
    def __init__(self):
        self.root = {} # 使用字典，而不是数组！key 可能为a，b,c...
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
            return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
            return True      
~~~

