class Solution():

	def rotate_matrix(self, matrix):
		if not matrix:
			return matrix
		N = len(matrix)
		for i in range(N/2):
			for j in range(N):
				matrix[i][j], matrix[N - 1 - i][j] = matrix[N - 1 - i][j], matrix[i][j]
		for i in range(N):
			for j in range(i + 1, N):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		return matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print "matrix before: "
for row in matrix:
	print row
Solution().rotate_matrix(matrix)
print "matrix after: "
for row in matrix:
	print row

matrix = [[ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]]
print "matrix before: "
for row in matrix:
	print row
Solution().rotate_matrix(matrix)
print "matrix after: "
for row in matrix:
	print row