class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data

    def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:  # 判断是否是空链表
            raise Exception('The list is an empty list')
        while cur_idx < idx - 1:  # 遍历链表
            cur = cur.next
            if cur is None:  # 判断是不是最后一个元素
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node

    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        if self.head is None:  # 空链表时
            raise Exception('The list is an empty list')
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        if idx == 0:  # 当删除第一个节点时
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:  # 当只有一个节点的链表时
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:  # 当删除的节点是链表最后一个节点时
            self.tail = cur

    def size(self):
        current = self.head
        count = 0
        if current is None:
            return 'The list is an empty list'
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         head = new_list = Node(0)
#
#         count = 1
#         while (l1 and l2):
#             print (id(new_list))
#             print (id(head))
#             print (id(l2))
#             print (id(l1))
#             print ('the index is:', count)
#             print_node(head)
#             print ('new_list:')
#             print_node(new_list)
#             if (l1.val < l2.val):
#                 new_list.next = l1
#                 l1 = l1.next
#             else:
#                 new_list.next = l2
#                 l2 = l2.next
#             new_list = new_list.next
#             count += 1
#
#
#         new_list.next = l1 or l2
#         return head.next

class Solution(object):

    def print_node(self, node):
        while node.next != None:
                print (node.val)
                node = node.next
        print (node.val)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## step 1
        ## define a new linked list and a dummy head, they have the same address
        cur = Node(0)
        dummy = cur
        ## step 2
        ## while l1 or l2 is not empty, compare their values
        while l1 and l2:
            if (l1.val < l2.val):
                ## step 3
                ## if l1's current value is smaller, attach l1 to the current list and move l1 to its next node
                cur.next = l1
                l1 = l1.next
            else:
                ## step 3
                ## if l2's current value is smaller, attach l2 to the current list and move l2 to its next node
                cur.next = l2
                l2 = l2.next
            ## step 4
            ## move current list to its next node to avoid overlap
            cur = cur.next ## cur becomes the reference to a new node object so will not influence

        cur.next = l1 or l2
        return dummy.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head.next:
        #     return head
        # cur = Node(0)
        # dummy = cur
        # while head.next:
        #     if head.val != head.next.val:
        #         cur.next = Node(head.val)
        #         head = head.next
        #         cur = cur.next
        #     else:
        #         head = head.next
        # cur.next = Node(head.val)
        # self.print_node(dummy.next)
        # return dummy.next


        if not head or not head.next:
            return head
        curr = head.next
        prev = head

        while (curr):
            if curr.val == prev.val:
                ## if the current value equal the previous value, it is duplicate and should be removed
                ## we first move the current node to its next, this operation will not influence the head
                ## we then attach the current node to the previous, so we remove the duplicate
                curr = curr.next
                prev.next = curr
            else:
                ## if the two values are not equal, then we keep the value and move the two nodes to their next
                ## this also will not influence the head, we just move the pointer
                prev = prev.next
                curr = curr.next
        return head

if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    [l1.append(x) for x in [1, 1, 2, 3, 3]]
    [l2.append(x) for x in [1, 3]]
    Solution().deleteDuplicates(l1.head)











