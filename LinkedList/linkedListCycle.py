class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head
def get_node(head, pos):
    if pos != -1:
        p = 0
        ptr = head
        while p < pos:
            ptr = ptr.next
            p += 1
        return ptr
class Solution(object):
    def hasCycle(self, head):
        hashS = set()
        while head:
            if head in hashS:
                return True
            hashS.add(head)
            head = head.next
        return False