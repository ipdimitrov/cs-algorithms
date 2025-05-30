from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        start = Node(0)
        curr_new = start
        curr_old = head
        size = 0
        while curr_old:
            curr_new.next = Node(curr_old.val)
            curr_new = curr_new.next
            curr_old = curr_old.next
            size+=1
        curr_new = start.next
        curr_old = head
        while curr_old:
            position = size
            rand_old = curr_old.random
            if rand_old is None:
                curr_new.random = None
            else:
                while rand_old:
                    rand_old = rand_old.next
                    position-=1
                rand_setter = start.next
                while position:
                    rand_setter = rand_setter.next
                    position-=1
                curr_new.random = rand_setter
            curr_new = curr_new.next
            curr_old = curr_old.next
        return start.next