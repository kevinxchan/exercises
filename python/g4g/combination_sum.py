# https://www.geeksforgeeks.org/combinational-sum/
# note: reusable integers

class Solution:

	def combination_sum(self, array, x):
		if not array or not x:
			return [[]]
		res = []
		self._backtrack(array, x, res, 0, [])
		res = sorted(res, key = lambda x: x[0])
		return res

	def _backtrack(self, array, x, res, curr_sum, curr_nums):
		if curr_sum == x:
			if sorted(curr_nums) not in res:
				res.append([v for v in curr_nums])
		else:
			for num in array:
				if curr_sum + num > x:
					continue
				self._backtrack(array, x, res, curr_sum + num, curr_nums + [num])

# TIME: O((n+k)!) where n is the number of elements, k is the max number of repeated elements
# SPACE: O(m) where m is the size of res
array = [2,4,6,8]
x = 8
solutions = Solution().combination_sum(array, x)
for solution in solutions:
	print solution
