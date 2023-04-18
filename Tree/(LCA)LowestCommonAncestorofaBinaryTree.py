# 외워야함 가장 낮은 공통 조상을 반환한다
class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def LCA(root, p, q):
    if root == None:
        return None
    
    left = LCA(root.left, p ,q)
    right = LCA(root.right, p ,q)
    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right

print(LCA([3,5,1,6,2,0,8,None,None,7,4],6,4))
    