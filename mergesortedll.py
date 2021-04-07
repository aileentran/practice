"""
Leetcode - 21. Merge Two Sorted Lists

input: head of 2 linked Lists
output: head of merged linked list

Thoughts
create a dummy node to catch empty ll cases
crate tail set to dummy node

loop through both lls --> neither ll not None
if l1 < l2
set tail to l1
increment l1 only
else l2 >= l1
set tail to l2
increment l2 only
outside if/else, increment tail = tail.next to keep making list

outside loop, in case there's any remaining nodes
add it to the tail

outside, return head of new list --> dummy.next
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(l1, l2):
    temp = ListNode()
    tail = temp

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        print(tail.val)

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return temp.next

def createLL(nums):
    ll = ListNode()
    tail = ll
    for num in nums:
        new = ListNode()
        new.val = num
        tail.next = new
        tail = tail.next

    return ll.next

l1 = createLL([1,2,4])
l2 = createLL([1,3,4])
# Output: [1,1,2,3,4,4]
l3 = createLL([])
l4 = createLL([])
# Output: []
l5 = createLL([])
l6 = createLL([0])
# Output: [0]

print(mergeTwoLists(l1, l2))
print(mergeTwoLists(l3, l4))
print(mergeTwoLists(l5, l6))
