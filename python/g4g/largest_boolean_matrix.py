# https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                candidate_area = [0]
                if grid[i][j] == 1:
                    self._dfs(grid, M, N, i, j, candidate_area)
                max_area = max(max_area, candidate_area[0])
        return max_area
    
    def _dfs(self, grid, num_rows, num_cols, curr_row, curr_col, candidate_area):
        if curr_row < 0 or curr_col < 0 or curr_row >= num_rows or curr_col >= num_cols or grid[curr_row][curr_col] != 1:
            return
        else:
            candidate_area[0] += 1
            grid[curr_row][curr_col] = "#"
            self._dfs(grid, num_rows, num_cols, curr_row - 1, curr_col, candidate_area)
            self._dfs(grid, num_rows, num_cols, curr_row + 1, curr_col, candidate_area)
            self._dfs(grid, num_rows, num_cols, curr_row, curr_col - 1, candidate_area)
            self._dfs(grid, num_rows, num_cols, curr_row, curr_col + 1, candidate_area)

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print Solution().maxAreaOfIsland(grid)

grid = [[0,0,0,0,0,0,0,0]]
print Solution().maxAreaOfIsland(grid)
