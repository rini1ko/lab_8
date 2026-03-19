from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    # Your code goes here.
    res= Node(data)
    res.next=head
    return res
def build_one_two_three():
    # Your code goes here.
    head=None
    for i in range(3,0, -1):
        head=push(head, i)
    return head