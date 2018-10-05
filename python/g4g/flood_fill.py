# https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/

from collections import deque

class Solution:

	def get_coord(self, x, y, M, N):
		return x > 0 and x < M and y > 0 and y < N

	def flood_fill(self, screen, x, y, new_color):
		if not screen:
			raise TypeError
		M = len(screen)
		N = len(screen[0])
		if x < 0 or x >= M or y < 0 or y >= N:
			raise ValueError
		q = deque()
		visited = [[False for _ in xrange(N)] for _ in xrange(N)]
		curr_color = screen[x][y]
		screen[x][y] = new_color
		q.append((x, y))
		visited[x][y] = True
		while q:
			curr_cell = q.popleft()
			new_x, new_y = curr_cell[0], curr_cell[1]
			T = self.get_coord(new_x - 1, new_y, M, N)
			B = self.get_coord(new_x + 1, new_y, M, N)
			L = self.get_coord(new_x, new_y - 1, M, N)
			R = self.get_coord(new_x, new_y + 1, M, N)
			if T and not visited[new_x - 1][new_y] and screen[new_x - 1][new_y] == curr_color:
				screen[new_x - 1][new_y] = new_color
				q.append((new_x - 1, new_y))
				visited[new_x - 1][new_y] = True
			if B and not visited[new_x + 1][new_y] and screen[new_x + 1][new_y] == curr_color:
				screen[new_x + 1][new_y] = new_color
				q.append((new_x + 1, new_y))
				visited[new_x + 1][new_y] = True
			if L and not visited[new_x][new_y - 1] and screen[new_x][new_y - 1] == curr_color:
				screen[new_x][new_y - 1] = new_color
				q.append((new_x, new_y - 1))
				visited[new_x][new_y - 1] = True
			if R and not visited[new_x][new_y + 1] and screen[new_x][new_y + 1] == curr_color:
				screen[new_x][new_y + 1] = new_color
				q.append((new_x, new_y + 1))
				visited[new_x][new_y + 1] = True
		return screen

screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]
print "screen before flood fill: "
for x in screen:
	print x
print "\n"

Solution().flood_fill(screen, 4, 4, 3)

print "screen after flood fill: "
for x in screen:
	print x
