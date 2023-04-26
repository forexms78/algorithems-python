def preorder(cur_node):
    if cur_node is None:
        return
    
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

preorder(root)

