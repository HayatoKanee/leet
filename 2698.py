from itertools import combinations


class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishment = 0
        for i in range(n):
            punishment += self.punishment(0, str(i * i), i)
        return punishment

    def punishment(self, index, num_str, target):
        if target == 0:
            return int(num_str)
        if target < 0:
            return 0
        if index == len(num_str):
            return 0
        for i in range(index, len(num_str)):
            punishment = self.punishment(index + 1, num_str, target - int(num_str[index: i + 1]))
            if punishment:
                return punishment
        return 0


n = 10
sol = Solution()
print(sol.punishmentNumber(n))
