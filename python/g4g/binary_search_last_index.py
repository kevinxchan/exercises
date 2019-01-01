def search(arr, target):
	if not arr:
		return -1
	return bsearch(arr, target, 0, len(arr) - 1)

def bsearch(arr, target, lo, hi):
	if lo > hi:
		return -1
	mid = (lo + hi) / 2
	if arr[mid] == target:
		if mid + 1 < len(arr):
			if arr[mid] == arr[mid+1]:
				return bsearch(arr, target, mid + 1, hi)
			else:
				return mid
		else:
			return mid
	elif arr[mid] < target:
		return bsearch(arr, target, mid + 1, hi)
	else:
		return bsearch(arr, target, lo, mid - 1)

print search([1,2,2,3,4], 2)
print search([1,2,2,3,4], 5)
print search([1,2,3,4,4,5,5,5,7,10,10], 5)
print search([1,2,3,4,4,5,5,5,7,10,10], 10)
print search([1,1,1,2,3,4,4,5,5,5,7,10,10], 1)