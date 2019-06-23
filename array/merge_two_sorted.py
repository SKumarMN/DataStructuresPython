# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        l3 = ListNode(-1)
        head = l3
        while(l1 != None and l2  != None):
            print("l1"+ str(l1.val))
            print("l2"+ str(l2.val))
            
            if(l1.val == l2.val):
                temp1 = ListNode(l2.val)
                temp2 = ListNode(l1.val)
                l3.next = temp1
                temp1.next = temp2
                l3= temp2
                l2 = l2.next
                l1 = l1.next
            elif(l1.val > l2.val):
                temp1 = ListNode(l2.val)
                l3.next = temp1
                l3= temp1
                l2 = l2.next
            else:
                temp1 = ListNode(l1.val)
                l3.next = temp1
                l3= temp1
                l1 = l1.next
                
        while(l1 != None ):
            temp1 = ListNode(l1.val)
            l3.next = temp1
            l3= temp1
            l1 = l1.next
        
        while(l2 != None):
            temp1 = ListNode(l1.val)
            l3.next = temp1
            l3= temp1
            l1 = l2.next
            
        return head.next


x = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
x.mergeTwoLists(l1,l2)

print(x.val)