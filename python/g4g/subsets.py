# https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/

class Solution:

	def subsets(self, array):
		if not array:
			return [[]]
		res = []
		array.sort()
		self._backtrack(array, res, [], -1)
		return res

	def _backtrack(self, array, res, curr, start):
		res.append([x for x in curr])
		for index, val in enumerate(array):
			if index > 0 and array[index] == array[index - 1]:
				continue
			if index > start:
				self._backtrack(array, res, curr + [val], index)

	def subsets_iterative(self, array):
		if not array:
			return [[]]
		res = [[]]
		seen = []
		for num in array:
			# [[], [1]] -2-> [[], [1], [2], [1,2]] -3-> [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
			res += [item + [num] for item in res if num not in seen]
			seen.append(num)
		return res

# TIME: O(2^n) since there exists 2^n subsets for a set, O(n * 2^n) for iterative approach (checking if num in seen).
# SPACE: O(2^n) to hold all the solutions in res.
array = [1, 2, 2, 3, 3, 3, 4, 2]
subsets = Solution().subsets(array)
# subsets = Solution().subsets_iterative(array)
for subset in subsets:
	print subset