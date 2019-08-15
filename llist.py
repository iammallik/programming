from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        q = deque()
        s = [] #stack
        cur = head
        l = 0 # list size
        
        while cur is not None:
            l += 1
            q.append(cur)
            s.append(cur)
            cur = cur.next
            
        if l <= 2:
            return
        
        q.popleft()
        cur = head
        cur.next = s.pop()
        nl = 2
        cur = cur.next
        print(l , nl)
        
        while nl < l:
            cur.next = q.popleft()
            cur = cur.next
            nl += 1
            print(l, nl)
            # break
            
            if nl < l:
                cur.next = s.pop()
                cur = cur.next
                nl += 1
                print(l, nl)
            
        return


if __name__ == '__main__':

    node2 = ListNode(3)
    node1 = ListNode(2)
    node = ListNode(1)
    node1.next = node2
    node.next = node1

    s = Solution()
    s.reorderList(node)






