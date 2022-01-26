import TreeGenerator
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)
            # else:
            #     result.append(0)
        inorder(root)
        return result[::-1] == result

if __name__ == '__main__':
    node_list = [
        {'data': '1', 'left': '2', 'right': '2', 'is_root': True},
        {'data': '2', 'left': '2', 'right': None, 'is_root': False},
        {'data': '2', 'left': None, 'right': None, 'is_root': False},
        {'data': '2', 'left': '2', 'right': None, 'is_root': False},
        {'data': '2', 'left': None, 'right': None, 'is_root': False},
    ]
    root = TreeGenerator.BinTreeNode.build_from(node_list)
    print (Solution().isSymmetric(root))