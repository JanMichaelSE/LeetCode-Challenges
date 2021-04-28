import unittest
from AddTwoNumbers import *

class Test_AddTwoNumbersMethods(unittest.TestCase):

    def test_example_1(self):
        # --- Arrange ---
        listNode_1 = ListNode(2,ListNode(4,ListNode(3))) # [2,4,3]
        listNode_2 = ListNode(5,ListNode(6,ListNode(4))) # [5,6,4]
        
        # --- Act ---
        returnedListNodes = Solution.addTwoNumbers(Solution,listNode_1, listNode_2)
        result_list = []
        while returnedListNodes is not None:
            result_list.append(returnedListNodes.val)
            returnedListNodes = returnedListNodes.next

        # --- Assert ----
        self.assertListEqual(result_list, [7,0,8])

    def test_example_2(self):
        # --- Arrange ---
        listNode_1 = ListNode() # [0]
        listNode_2 = ListNode() # [0]
        
        # --- Act ---
        returnedListNodes = Solution.addTwoNumbers(Solution,listNode_1, listNode_2)
        result_list = []
        while returnedListNodes is not None:
            result_list.append(returnedListNodes.val)
            returnedListNodes = returnedListNodes.next
            
        # --- Assert ----
        self.assertListEqual(result_list, [0])

    def test_example_3(self):
        # --- Arrange ---
        listNode_1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))) # [9,9,9,9,9,9,9]
        listNode_2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9)))) # [9,9,9,9]
        
        # --- Act ---
        returnedListNodes = Solution.addTwoNumbers(Solution,listNode_1, listNode_2)
        result_list = []
        while returnedListNodes is not None:
            result_list.append(returnedListNodes.val)
            returnedListNodes = returnedListNodes.next

        # --- Assert ----
        self.assertListEqual(result_list, [8,9,9,9,0,0,0,1])

if __name__ == '__main__':
    unittest.main()