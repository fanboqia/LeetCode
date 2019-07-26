# -*- coding:utf-8 -*-
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        # write your code here
        if head == None:
            return head
        root = head
        tail = None
        listSize = 0
        while root != None:
            listSize = listSize + 1
            if root.next == None:
                tail = root
            root = root.next
        k = k % listSize
        if k == 0:
            return head
        i = 0
        start = head
        while i < listSize - k - 1:
            start = start.next
            i = i + 1
        tail.next = head
        head = start.next
        start.next = None
        return head

node3 = ListNode(3,None)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)
node0 = ListNode(0,node1)

list = Solution().rotateRight(node0,2)
while list != None:
    print list.val
    list = list.next




