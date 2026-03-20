class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise TypeError
    first_head=head
    second_head=head.next
    t_first=first_head
    t_second=second_head
    while t_first.next and t_second.next:
        t_first.next=t_first.next.next
        t_second.next=t_second.next.next
        t_first=t_first.next
        t_second=t_second.next
    t_first.next=None
    return Context(first_head, second_head)