class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeList(list1, list2):
            dummy = ListNode(0)
            current = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 or list2
            return dummy.next

        for i in range(1, len(lists)):
            lists[i] = mergeList(lists[i-1], lists[i])

        return lists[-1]