import unittest
from CustomLinkedList import CustomLinkedList
from User import User


class CustomLinkedListTest(unittest.TestCase):


    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.starting_list = None


    def setUp(self):
        self.starting_list = CustomLinkedList()
        user = User("Rino", "Campa")
        user2 = User("Chetto", "Wis")
        self.starting_list.add(user)
        self.starting_list.add(user2)


    def test_add_element_at_the_end(self):
        user3 = User("Rollo", "Ape")
        self.starting_list.add(user3)
        self.assertEqual(self.starting_list.get(2).get_surname(), "Ape")


    def test_add_element_at_the_beginning(self):
        user3 = User("Rollo", "Ape")
        self.starting_list.add_at_beginning(user3)
        self.assertEqual(self.starting_list.get(0).get_surname(), "Ape")


    def test_remove_second_element(self):
        self.starting_list.remove(1)
        self.assertEqual(self.starting_list.length(), 1)


    def test_length(self):
        self.assertEqual(self.starting_list.length(), 2)



if __name__ == '__main__':
    unittest.main()