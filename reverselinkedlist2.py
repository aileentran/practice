"""
Leetcode - 206. Reverse Linked List

input: head of linked list
output: head of reversed linked list

Thoughts
prev variable set to None
curr set to head of ll

loop through linked list while curr is NOT none
temp variable = curr.next
set curr.next to prev
scoot prev to curr node
scoot curr node to temp value

outside loop, return value
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverseList(head):
    return

head1 = [1,2,3,4,5] #[5,4,3,2,1]
head2 = [1,2] #[2,1]
head3 = [] #[]
