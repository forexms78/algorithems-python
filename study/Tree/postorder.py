def postorder(cur_node):
    if cur_node is None:
        return
    
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)


postorder(root)

#GHDEBFCA