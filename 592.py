import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        tokens = re.findall(r'[+-]?\d+/\d+', expression)
        sign = '+'
        numerator, denominator = 0, 1
        for token in tokens:
            n, d = int(token.split('/')[0]), int(token.split('/')[1])
            n *= denominator
            numerator = numerator * d + n
            denominator *= d
            divisor = self.gcd(numerator, denominator)
            numerator //= divisor
            denominator //= divisor
            # print(numerator, denominator)
        return f"{numerator}/{denominator}"

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)


expression = "1/3-1/2"
s = Solution()
print(s.fractionAddition(expression))
