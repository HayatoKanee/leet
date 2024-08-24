
class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishment = 0
        for i in range(1,n+1):
            if self.punishment(0,0, str(i * i), i):
                punishment += i*i
        return punishment

    def punishment(self, added,cached_sum,num_str, target):
        if not num_str:
            return target == added + cached_sum
        num = int(num_str[0])
        return self.punishment(added,cached_sum*10+num,num_str[1:], target) or self.punishment(added+num,cached_sum,num_str[1:], target)