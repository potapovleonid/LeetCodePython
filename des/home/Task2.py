# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1: list, l2: list):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        class Solution(object):
            def addTwoNumbers(self, l1, l2):
                """
                :type l1: ListNode
                :type l2: ListNode
                :rtype: ListNode
                """
                first_number = ''
                index = l1
                while True:
                    first_number += str(index.val)
                    if index.next is None:
                        break
                    index = index.next
                first_number = int(''.join(first_number[::-1]))

                index = l2
                second_number = ''
                while True:
                    second_number += str(index.val)
                    if index.next is None:
                        break
                    index = index.next
                second_number = int(''.join(second_number[::-1]))
                sum_arr = first_number + second_number
                sum_arr = [int(x) for x in str(sum_arr)][::-1]
                result = None
                index = None
                for i in sum_arr:
                    if result is None:
                        result = ListNode(i, None)
                        index = result
                    else:
                        index.next = ListNode(i, None)
                        index = index.next
                return result


l1 = [2, 4, 3]
l2 = [5, 6, 4]

s = Solution()
assert s.addTwoNumbers(l1, l2) == [7, 0, 8]
