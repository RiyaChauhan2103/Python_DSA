# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            curr=head
            # print(curr)
            while curr.next is not None:
                next_ele=curr.next
                if curr.val==next_ele.val:
                    curr.next=next_ele.next
                else:
                    curr=curr.next
        return head