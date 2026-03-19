from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    dummy=Node(0)
    dummy.next=head
    prev=dummy
    while prev.next and prev.next.next:
        cur=prev.next
        next=prev.next.next
        
        cur.next=next.next
        next.next=cur
        prev.next=next

        prev=cur
        
    return dummy.next