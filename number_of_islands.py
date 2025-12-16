class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen = set()
        islands = 0
        def explore_island(i,j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if grid[i][j] == "1" and (i,j) not in seen:
                    seen.add((i,j))
                    explore_island(i+1, j)
                    explore_island(i, j+1)
                    explore_island(i-1, j)
                    explore_island(i, j-1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(i)
                print(j)
                print(grid[i][j])
                print("is it seen?", (i,j) in seen)
                if (i,j) in seen:
                    continue
                else:
                    print("ran non seen")
                    if grid[i][j] == "1":
                        print("grid of i j is one")
                        islands += 1
                        explore_island(i,j)

        return islands
