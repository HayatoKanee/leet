# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        new_list_head = ListNode()
        current = new_list_head
        while head:
            if head.val not in nums:
               current.next = ListNode(head.val)
               current = current.next
            head = head.next
        return new_list_head.next