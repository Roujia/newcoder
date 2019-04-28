# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        value_list=[]
        head=listNode
        while head is not None:
            value_list.append(head.val)
            head=head.next
        value_list.reverse()
        return value_list

if __name__=="__main__":
    s=Solution()
    N1=ListNode(1)
    # N1.next=ListNode(2)
    # N1.next.next=ListNode(5)
    p = N1
    for i in range(2,9,2):
        p.next=ListNode(i)
        p=p.next
    print(s.printListFromTailToHead(N1))