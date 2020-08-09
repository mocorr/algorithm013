'''
49. 字母异位词分组
1. key -- 字典中要查找的键。
2. default -- 如果指定键的值不存在时，返回该默认值。
这一题其实并未有太多的自我理解
'''
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dict = {}
    for item in strs:
        key = tuple(sorted(item))
        dict[key] = dict.get(key, []) + [item]
    return list(dict.values())
