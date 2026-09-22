class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        if not head or not head.next:
            return head

        l, r = head, self.findmid(head)

        temp = r.next
        r.next = None
        r = temp

        l = self.sortList(l)
        r = self.sortList(r)

        return self.merge(l, r)

    def findmid(self, head):
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        return s

    def merge(self, l, r):
        dummy = tail = ListNode()

        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next

            tail = tail.next

        if l:
            tail.next = l

        if r:
            tail.next = r

        return dummy.next