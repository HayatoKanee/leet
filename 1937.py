from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        mp = [[0 for _ in range(len(points[i]))] for i in range(len(points))]
        for i in range(len(points[0])):
            mp[0][i] = points[0][i]
        for i in range(1, len(points)):
            current_point = 0
            for j in range(len(points[i - 1])):
                current_point = max(current_point - 1, mp[i - 1][j])
                mp[i][j] = current_point
            for j in range(len(points[i]) - 1, -1, -1):
                current_point = max(current_point - 1, mp[i - 1][j])
                mp[i][j] = max(current_point,mp[i][j]) + points[i][j]
        return max(mp[-1])


# points = [[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]
# sol = Solution()
# print(sol.maxPoints(points))
