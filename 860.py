from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                change[10] += 1
                if change[5] == 0:
                    return False
                change[5] -= 1
            else:
                if change[10] == 0:
                    if change[5] < 3:
                        return False
                    change[5] -= 3
                else:
                    change[10] -= 1
                    if change[5] == 0:
                        return False
                    change[5] -= 1
        return True
