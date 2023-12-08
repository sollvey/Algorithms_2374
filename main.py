from BinTree import BinaryTree
from AVL_Tree import AVLTree
from DynamicArray import DynamicArray
from Stack import Stack


binary_tree = BinaryTree()
binary_tree_from_file = binary_tree.parsing_bracket_string()
binary_preorder = binary_tree_from_file.pre_order_travers(binary_tree_from_file)
print("BINARY PREORDER: ", binary_preorder.array[:len(binary_preorder)])
avl_tree = AVLTree()
avl_from_binary = avl_tree.binary2avl(binary_tree_from_file)
avl_preorder = avl_from_binary.pre_order_travers(avl_from_binary)
print("AVL PREORDER: ", avl_preorder.array[:len(avl_preorder)])
avs_inorder = avl_from_binary.in_order_travers(avl_from_binary)
print("AVL INORDER: ", avs_inorder.array[:len(avs_inorder)])
print("AVL POSTORDER: ", avl_from_binary.post_order_travers(avl_from_binary))
print("AVL BFS: ", end="")
avl_from_binary.width_travers(avl_from_binary)
