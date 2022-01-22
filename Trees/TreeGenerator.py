class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    @classmethod
    def build_from(cls, node_list):
        """通过节点信息构造二叉树
        第一次遍历我们构造 node 节点
        第二次遍历我们给 root 和 孩子赋值
        最后我们用 root 初始化这个类并返回一个对象
        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return root

if __name__ == '__main__':
    BinTreeNode(5)