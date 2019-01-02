class TreeNode():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def closestElementBST(root, K):
	def traverse(root, K, global_min, ret):
		if not root:
			return
		elif abs(K - root.val) == 0:
			ret[0] = root.val
		else:
			if global_min > abs(K - root.val):
				global_min = abs(K - root.val)
				ret[0] = root.val
			if root.val > K:
				traverse(root.left, K, global_min, ret)
			else:
				traverse(root.right, K, global_min, ret)
	if not root:
		return None
	global_min = float("inf")
	ret = [None]
	traverse(root, K, global_min, ret)
	return ret[0]

root = TreeNode(9)
root.left = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(7)
root.right = TreeNode(17)
root.right.right = TreeNode(22)
root.right.right.left = TreeNode(20)

print closestElementBST(root, 4)
print closestElementBST(root, 18)
print closestElementBST(root, 12)