var swapPairs = function(head) {
    if(head === null || head.next === null)
        return head
    var previous  = null;
    var current   = head;
    var following = (head.next != null) ? head.next.next : null;
    head = head.next;
    
    while(current !== null && current.next !== null) {
        var next = current.next;
        next.next = current; 
        if(previous != null)
            previous.next = next;
        current.next = following;    
        previous = current;
        current = following;
        following = (current !== null && current.next != null) ? current.next.next : null;
    }
    
    return head;
};