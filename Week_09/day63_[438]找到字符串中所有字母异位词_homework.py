# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表 
#  👍 377 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        res = []
        p_cnt, window = dict(), dict()
        for ch in p:
            p_cnt[ch] = p_cnt.get(ch, 0) + 1

        left, right = 0, 0
        while right < len(s):
            if s[right] not in p_cnt:
                left, right = right + 1, right + 1
                window = dict()
            else:
                window[s[right]] = window.get(s[right], 0) + 1
                if right - left + 1 == len(p):
                    if p_cnt == window:
                        res.append(left)
                    window[s[left]] -= 1  # 等于0时也无需删除 因为window不统计非目标字母
                    left += 1
                right += 1
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
