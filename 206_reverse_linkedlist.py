class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last, cur = None, head
        while cur:
            nxt=cur.next
            cur.next=last
            last=cur
            cur=nxt
        return last