class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    # your code goes here.
    if not head or not head.next:
        return head
    new_node=reverse(head.next)
    head.next.next=head
    head.next=None
    return new_node