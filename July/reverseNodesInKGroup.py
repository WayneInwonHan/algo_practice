class Solution:
    def reverseKGroup(self, head, k):
        def reverse(head, k):
            p = head
            for i in range(k):
                if(p):
                    p = p.next
                else:
                    return head

            pre, now = head, head.next
            pre.next = None
            i = 1
            while(now != None and i < k):
                nex = now.next
                now.next = pre
                pre, now = now, nex
                i += 1

            if(now != None):
                head.next = reverse(now, k)

            return pre

        if(head):
            return reverse(head, k)
        else:
            return None