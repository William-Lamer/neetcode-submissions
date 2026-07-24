# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return None
 
        
        if list1.val <= list2 .val:
            list3head = ListNode(list1.val)
            list1 = list1.next
        else:
            list3head = ListNode(list2.val)
            list2 = list2.next

        curr = list3head
        while list1 or list2:
            if (list1 and list2) and (list1.val <= list2.val):
                curr.next = list1
                list1 = list1.next
            elif (list1 and list2) and (list1.val > list2.val):
                curr.next = list2
                list2 = list2.next
            elif (list1 and not list2):
                curr.next = list1
                list1 = list1.next
            elif list2 and not list1:
                curr.next = list2
                list2 = list2.next

            if curr.next:
                curr = curr.next


        curr = list3head
        while curr:
            print(curr.val)
            curr = curr.next


        return list3head