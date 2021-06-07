class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        reversed_head = self.reverse(head)

        while (head != None and reversed_head != None):

            if (head.val != reversed_head.val):
                return False
            
            head = head.next
            reversed_head = reversed_head.next
        
        return True
    
    def reverse(self, head):        
        prev = None
                
        dummy = ListNode(0)
        dummy.next = head
        current = head
                
        while (current != None):
            new = ListNode(current.val)
            new.next = prev
            prev = new
            current = current.next
        
        head = dummy.next
        
        return prev