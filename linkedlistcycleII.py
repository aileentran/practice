"""
Leetcode - 142. Linked List Cycle II

input: head of list
return: node where cycle begins or null/None
"""

def detectCycle(head):
    if head == None:
        return None

    seen = []
    curr = head

    while curr.next:
        if curr in seen:
            return curr
        seen.append(curr)
        curr = curr.next

    return None
