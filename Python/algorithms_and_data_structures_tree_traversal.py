""" Tree traversals:
    1)  preorder:   root, left, right 
    2)  inorder:    left, root, right
    3)  postorder:  left, right, root
"""
class Tree(object):
    'A simple Tree node class'
    def __init__(self, x=0, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r

### ============================== RECURSIVE ============================== 

def print_preorder(root):
    'Recursively traverse the tree in preorder and print elements'
    if root is None:
        return
    # else:    
    print(root.x, end=" ")
    print_preorder(root.l)
    print_preorder(root.r)
    pass

def print_inorder(root):
    'Recursively traverse the tree in inorder and print elements'
    if root is None:
        return
    # else:    
    print_inorder(root.l)
    print(root.x, end=" ")
    print_inorder(root.r)
    pass

def print_postorder(root):
    'Recursively traverse the tree in postorder and print elements'
    if root is None:
        return
    # else:    
    print_postorder(root.l)
    print_postorder(root.r)
    print(root.x, end=" ")
    pass

### ============================== ITERATIVE ============================== 
#   ============================== deprecated ============================= 

def print_preorder_iter_first_thougt(root):
    'Iteratively traverse the tree in preorder and print elements'
    # This doesn't generalize well to inorder.
    # Postorder could be achived, by turning visiting in reverse preorder,
    # and using another stack to store the visits and reverse them by popping the elements,
    # so this approach should be dropped.
    
    if root is None:
        return
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr.x, end=" ")
        if curr.r is not None:
            stack.append(curr.r)
        if curr.l is not None:
            stack.append(curr.l)
    pass

### ============================== ITERATIVE ============================== 
#   ============================== one stack ============================== 

def print_preorder_iter(root):
    'Iteratively traverse the tree in preorder and print elements'
    'Uses one stack'
    stack = []  # start with an empty stack
    curr = root # and root as the current node
    while (curr is not None) or (len(stack) > 0):
        # go as deep as possible to the left of the curr node
        while (curr is not None):
            print(curr.x, end=" ")  # visit each node along the way
            stack.append(curr)      # and push the nodes along the way
            curr = curr.l
        # curr is now None
        # the leftmost element is on the top of stack
        
        curr = stack.pop()  # get the root

        curr = curr.r   # go to the right subtree
    pass

def print_inorder_iter(root):
    'Iteratively traverse the tree in inorder and print elements'
    'Uses one stack'
    stack = []  # start with an empty stack
    curr = root # and root as the current node
    while (curr is not None) or (len(stack) > 0):
        # go as deep as possible to the left of the curr node
        while (curr is not None):
            stack.append(curr)  # and push the nodes along the way
            curr = curr.l
        # curr is now None
        # the leftmost element is on the top of stack

        curr = stack.pop()  # get the root
        print(curr.x, end=" ")

        curr = curr.r   # go to the right subtree
    pass


def print_postorder_iter(root):
    'Iteratively traverse the tree in postorder and print elements'
    'Uses one stack'
    stack = []  # start with an empty stack
    curr = root # and root as the current node.
    prev = None # points to the previously visited node
    top = None  # top of the stack
    while (curr is not None) or (len(stack) > 0):
        # go as deep as possible to the left of the curr node
        if curr is not None:
            stack.append(curr)  # and push the nodes along the way
            curr = curr.l
            continue
        else:
            top = stack[-1]
            if (top.r is not None) and (top.r != prev):
                curr = top.r
                continue
            prev = stack.pop()
            print(prev.x, end=" ")
    return

### ============================== MORRIS ============================== 
#   ============================== const. ============================== 

def print_preorder_morris(root):
    curr = root
    while curr is not None:
        if curr.l is None:
        # if there is no left subtree, visit the node, and go to the right subtree
            print(curr.x, end=" ")
            curr = curr.r
        else:
        # if there is, visit the left subtree
            # first find the curr's inorder predecessor in the left subtree
            pre = curr.l
            while   (pre.r is not None) and \
                    (pre.r != curr):    # this detects a cycle if we've already linked the pre.r to the curr,
                                        # and have returned from the left subtree
                pre = pre.r
            
            if pre.r is None:
            # if we haven't linked the pre.r to curr, and been to the left subtree,
            # do that,
                print(curr.x, end=" ")  # but first visit the node
                pre.r = curr
                curr = curr.l
            else:
            # if we have, remove the uplink and go to the right subtree
                pre.r = None
                curr = curr.r

def print_inorder_morris(root):
    curr = root
    while curr is not None:
        if curr.l is None:
        # if there is no left subtree, visit the node, and go to the right subtree
            print(curr.x, end=" ")
            curr = curr.r
        else:
        # if there is, visit the left subtree
            # first find the curr's inorder predecessor in the left subtree
            pre = curr.l
            while   (pre.r is not None) and \
                    (pre.r != curr):    # this detects a cycle if we've already linked the pre.r to the curr,
                                        # and have returned from the left subtree
                pre = pre.r
            
            if pre.r is None:
            # if we haven't linked the pre.r to curr, and been to the left subtree, do that:
                pre.r = curr
                curr = curr.l
            else:
            # if we have, remove the uplink, visit the node, and go to the right subtree
                print(curr.x, end=" ")
                pre.r = None
                curr = curr.r

def print_postorder_morris(root):
    curr = Tree(0, root, None) # a dummy node    
    while curr is not None:
        if curr.l is None:
        # if there is no left subtree, go to the right subtree
            curr = curr.r
        else:
        # if there is, visit the left subtree
            # first find the curr's inorder predecessor in the left subtree
            pre = curr.l
            while   (pre.r is not None) and \
                    (pre.r != curr):    # this detects a cycle if we've already linked the pre.r to the curr,
                                        # and have returned from the left subtree
                pre = pre.r
            
            if pre.r is None:
            # if we haven't linked the pre.r to curr, and been to the left subtree, do that:
                pre.r = curr
                curr = curr.l
            else:
            # if we have (this is the tricky part for postorder):
                # reverse the right references in chain from pre to curr
                first = curr
                middle = curr.l
                while middle != curr:
                    last = middle.r
                    middle.r = first
                    first = middle
                    middle = last
                
                # visit the nodes from pre to curr
                # again, reverse the right references from pre to curr
                first = curr
                middle = pre
                while middle != curr:
                    print(middle.x, end=" ")
                    last = middle.r
                    middle.r = first
                    first = middle
                    middle = last
                
                # remove the uplink and go to the right subtree
                pre.r = None
                curr = curr.r


### ============================== TESTING ============================== 

T = Tree(0
        , Tree(1
            , Tree(3)
            , Tree(4)
        )
        , Tree(2
            , Tree(5)
            , Tree(6)
        )
    )
""" T :
              0
        1           2
    3       4   5       6
"""

print("preorder print, rec, iter, Morris:")
print_preorder(T)
print()
print_preorder_iter(T)
print()
print_preorder_morris(T)
print()

print("inorder print, rec, iter, Morris:")
print_inorder(T)
print()
print_inorder_iter(T)
print()
print_inorder_morris(T)
print()

print("postorder print, rec, iter, Morris:")
print_postorder(T)
print()
print_postorder_iter(T)
print()
print_postorder_morris(T)
print()
