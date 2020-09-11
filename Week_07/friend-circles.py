class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        p = [[i] for i in range(n)]
        ans = n
        for i, j in itertools.combinations(range(n), 2):
            if M[i][j] and p[i] is not p[j]:
                if len(p[i]) < len(p[j]):   #权重比较
                    i, j = j, i             #优先让小集合并入大集合
                p[i].extend(p[j])
                for k in p[j]:
                    p[k] = p[i]
                ans -= 1
        return ans
