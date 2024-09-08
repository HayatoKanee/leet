# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = []
        split_list = []
        count = 0
        while head:
            temp.append(head)
            head = head.next
            count += 1
        num_of_elements = count // k
        num_of_ones = count % k
        index = 0
        for _ in range(k):
            if index >= count:
                split_list.append(None)
            else:
                if num_of_ones:
                    temp[index + num_of_elements].next = None
                    num_of_ones -= 1
                    split_list.append(temp[index])
                    index += 1
                else:
                    temp[index + num_of_elements - 1].next = None
                    split_list.append(temp[index])
            index += num_of_elements
        return split_list
