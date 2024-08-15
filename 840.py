from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                if self.is_magic_square(grid, row, col):
                    count += 1
        return count

    def is_magic_square(self, grid, row, col):
        seen = [False] * 10
        for i in range(3):
            for j in range(3):
                val = grid[row + i][col + j]
                if val < 1 or val > 9:
                    return False
                if seen[val]:
                    return False
                seen[val] = True
        rows = [0] * 3
        for i in range(3):
            for j in range(3):
                rows[i] += grid[row + j][col + i]
        if not (rows[0] == rows[1] == rows[2]):
            return False
        cols = [0] * 3
        for i in range(3):
            for j in range(3):
                cols[i] += grid[row + i][col + j]
        if not (cols[0] == cols[1] == cols[2]):
            return False
        diags = [0] * 2
        for i in range(3):
            diags[0] += grid[row + i][col + i]
            diags[1] += grid[row + 2 - i][col + i]
        if not (diags[0] == diags[1]):
            return False
        return True
