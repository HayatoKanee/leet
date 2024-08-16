class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_count = [0 for _ in range(n)]
        a_count = [0 for _ in range(n)]
        count = 0
        for i in range(n):
            b_count[i] = count
            if s[i] == 'b':
                count += 1

        count = 0
        for i in range(n - 1, -1, -1):
            a_count[i] = count
            if s[i] == 'a':
                count += 1

        min_del = n
        for i in range(n):
            min_del = min(b_count[i] + a_count[i], min_del)
        return min_del


sol = Solution()
s = "aababbab"
print(sol.minimumDeletions(s))
