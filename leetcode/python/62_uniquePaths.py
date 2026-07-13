class Solution():
    def __init__(self):
        self.memo = dict()
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        else:
            if (m - 1, n) not in self.memo.keys(): self.memo[(m - 1, n)] = self.uniquePaths(m - 1, n)
            if (m, n - 1) not in self.memo.keys(): self.memo[(m, n - 1)] = self.uniquePaths(m, n - 1)
            p1 = self.memo[(m - 1, n)]
            p2 = self.memo[(m, n - 1)]
            return p1 + p2
