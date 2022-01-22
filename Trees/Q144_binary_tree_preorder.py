import TreeGenerator
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def return_node_value(node):
            result.append(node.data)
            if node.left != None:
                return_node_value(node.left)
            if node.right != None:
                return_node_value(node.right)
        return_node_value(root)
        return result

if __name__ == '__main__':
    node_list = [
        {'data': '1', 'left': '2', 'right': '3', 'is_root': True},
        {'data': '2', 'left': '4', 'right': '5', 'is_root': False},
        {'data': '3', 'left': None, 'right': None, 'is_root': False},
        {'data': '4', 'left': None, 'right': None, 'is_root': False},
        {'data': '5', 'left': None, 'right': None, 'is_root': False},
    ]
    root = TreeGenerator.BinTreeNode.build_from(node_list)
    print (Solution().preorderTraversal(root))