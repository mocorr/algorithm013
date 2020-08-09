# 异位词：简单理解为单词排序不一样；但出现次数一样

# 法一：暴力排序法
# 排序完成后，如果相等则为True
import collections


def isAnagrem1(s, t):
    return sorted(s) == sorted(t)


# 法二：哈希
# 记录每一个字母，然后放入一个表里面，一个生产、一者消费，若二者恰好均等则


def isAnagram2(self, s: str, t: str) -> bool:
    dicts = collections.defaultdict(int)
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        dicts[s[i]] = dicts[s[i]] + 1
        dicts[t[i]] = dicts[t[i]] - 1
    for val in dicts.values():
        if val != 0:
            return False
    return True


# 法三:分割求值法
# 由题意可知当长度不相等时，一定不为异位词，直接return掉
# 集合 + 计数
def isAnagram3(s: str, t: str):
    if len(s) != len(t):
        return False
    elif set(s) == set(t):
        for i in set(t):
            if s.count(i) != t.count(i):
                return False
        return True
    else:
        return False
