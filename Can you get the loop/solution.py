def loop_size(node):
    slow=node
    fast=node
    slow=slow.next
    fast=fast.next.next
    while slow!=fast:
        slow=slow.next
        fast=fast.next.next
    count=1
    while slow.next!=fast:
        slow=slow.next
        count+=1
    return count
