# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# note: for unique characters only

class Solution:

	def permutations(self, string):
		if not string:
			return ['']
		res = []
		string = "".join(sorted(string))
		self._backtrack(string, len(string), res, [])
		return res

	def _backtrack(self, string, input_length, res, curr):
		if input_length == len(curr):
			res.append("".join([x for x in curr]))
		else:
			for sub in string:
				if sub in curr:
					continue
				self._backtrack(string, input_length, res, curr + [sub])

# TIME: O(n!)
# SPACE: O(n!) -> O(n) for recursion depth, but O(n!) different solutions in res
string = "abcd"
solutions = Solution().permutations(string)
for solution in solutions:
	print solution