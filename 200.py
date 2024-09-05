from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowlimit = len(grid)
        collimit = len(grid[0])
        seen = [[False] * collimit for _ in range(rowlimit)]
        count = 0
        for i in range(rowlimit):
            for j in range(collimit):
                if not seen[i][j] and grid[i][j] == '1':
                    count +=1
                    self.flood(i,j,rowlimit,collimit,grid,seen)
        return count
    def flood(self,row,col,rowlimit,collimit,grid: List[List[str]],seen:List[List[bool]]):
        if row >= rowlimit or row < 0:
            return
        if col >= collimit or col < 0:
            return
        if grid[row][col] == '0':
            return
        if seen[row][col]:
            return
        seen[row][col] = True
        self.flood(row+1,col,rowlimit,collimit,grid,seen)
        self.flood(row, col+1, rowlimit,collimit,grid,seen)
        self.flood(row-1,col,rowlimit,collimit,grid,seen)
        self.flood(row,col-1,rowlimit,collimit,grid,seen)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
sol = Solution()
print(sol.numIslands(grid))