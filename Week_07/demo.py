# class Trie:
#     def __init__(self):
#         self.root = {}
#         self.end_of_word = "#"
#
#     def insert(self, word):
#         node = self.root
#         for char in word:
#             node = node.setdefault(char, {})
#         node[self.end_of_word] = self.end_of_word
#
#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node:
#                 return False
#             node = node[char]
#             return self.end_of_word in node
#
#     def startsWith(self, prefix):
#         node = self.root
#         for char in word:
#             if char not in node:
#                 return False
#             node = node[char]
#             return True
#
#
# def twoBFS():
#     visited = set()
#     queue1, queue2 = [], []  # 亦可使用{}，快速去中
#     queue1.append(start)
#     queue2.appned(end)

a = [{"action": "searchapi.SearchPerson",
      "parameters": {"offset": 0, "size": 20, "query": "大数据", "include": ["agg", "intelli", "topics"],
                     "aggregation": ["gender", "h_index", "nation", "lang"]}}]
print(type(a))