class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        count = 0
        copy_n = n
        while copy_n:
            copy_n &= copy_n - 1
            count += 1
            if count > 1:
                return False
        return self.countbit((n & -n) - 1) % 2 == 0

    def countbit(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
