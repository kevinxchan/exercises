class Solution:

	def compress(self, string):
		if not string:
			return string
		new_string = ""
		prev, count = string[0], 1
		for sub in string[1:]:
			if sub == prev:
				count += 1
			else:
				new_string = new_string + prev + str(count)
				prev, count = sub, 1
		new_string = new_string + prev + str(count)
		return new_string if len(new_string) < len(string) else string

# TIME: O(n) since one pass through the string
# SPACE: O(1) 
string = "aabcccccaaa"
print Solution().compress(string)
string = "Abba"
print Solution().compress(string)