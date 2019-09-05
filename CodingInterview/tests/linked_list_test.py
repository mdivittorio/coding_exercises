import unittest
from coding_exercises.CodingInterview.utils import LinkedList


class TestLinkedList(unittest.TestCase):
    # add
    def test_add_empty_length(self):
        ll = LinkedList()
        ll.add(5)
        self.assertEqual(len(ll), 1)

    def test_add_non_empty_length(self):
        ll = LinkedList.get_linked_list(1, 2)
        ll.add(5)
        self.assertEqual(len(ll), 3)

    def test_add_empty_value(self):
        ll = LinkedList()
        ll.add(5)
        self.assertTrue(ll.find(5))

    def test_add_non_empty_value(self):
        ll = LinkedList.get_linked_list(1, 2)
        ll.add(5)
        self.assertTrue(ll.find(5))

    # delete_index
    def test_delete_index_empty(self):
        ll = LinkedList()
        ll.delete_index(2)
        self.assertEqual(len(ll), 0)

    def test_delete_index_existing_length(self):
        ll = LinkedList.get_linked_list(1, 2)
        ll.delete_index(1)
        self.assertEqual(len(ll), 1)

    def test_delete_index_existing_value(self):
        ll = LinkedList.get_linked_list(1, 2)
        ll.delete_index(1)
        self.assertFalse(ll.find(2))

    def test_delete_neg_index_last(self):
        ll = LinkedList.get_linked_list(1, 2)
        ll.delete_index(-1)
        self.assertFalse(ll.find(2))

    def test_delete_neg_index_first(self):
        ll = LinkedList.get_linked_list(1, 2)
        ll.delete_index(-2)
        self.assertFalse(ll.find(1))

    def test_delete_oob_index(self):
        with self.assertRaises(IndexError):
            LinkedList.get_linked_list(1).delete_index(1)

    # delete_value
    def test_delete_value_empty(self):
        assert LinkedList().delete_val(0) is None

    def test_delete_missing_value(self):
        ll = LinkedList.get_linked_list(1, 2, 3)
        ll.delete_val(4)
        self.assertEqual(len(ll), 3)
