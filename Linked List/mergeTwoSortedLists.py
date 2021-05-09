class ListNode:
    def __init__(self, data, next = None):
        self.val = data
        self.next = next
    def make_list(elements):
        head = ListNode(elements[0])
        for element in elements[1:]:
            ptr = head
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(element)
        return head
def print_list(head):
    ptr = head
    print('[', end = "")
    while ptr:
        print(ptr.val, end = ", ")
        ptr = ptr.next
    print(']')
class Solution:
    def mergeTwoLists(self, l1, l2):
        
        if not l1:
            return l2
        if not l2:
            return l1
        if(l1.val<=l2.val):
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2