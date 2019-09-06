import unittest
from list import List


class TestList__init__(unittest.TestCase):

    def test_init_with_one_object(self):
        list1 = List(1)
        list2 = List('well')
        list3 = List({'first': 'second'})
        self.assertEqual(str(list1), '[1]')
        self.assertEqual(len(list1), 1)

        self.assertEqual(str(list2), '[well]')
        self.assertEqual(len(list2), 1)

        self.assertEqual(str(list3), "[{'first': 'second'}]")
        self.assertEqual(len(list3), 1)

    def test_init_with_default_list(self):
        list1 = List([1, "sda", 6])
        list2 = List([1])
        list3 = List([])

        self.assertEqual(str(list1), "[1, sda, 6]")
        self.assertEqual(len(list1), 3)

        self.assertEqual(str(list2), "[1]")
        self.assertEqual(len(list2), 1)

        self.assertEqual(str(list3), "[]")
        self.assertEqual(len(list3), 0)

    def test_init_with_List(self):
        list1 = List([1, 2, 3])
        list2 = List(list1)
        list3 = List(List())
        self.assertEqual(str(list2), "[1, 2, 3]")
        self.assertEqual(len(list2), 3)

        self.assertEqual(str(list3), "[]")
        self.assertEqual(len(list3), 0)

    def test_empty_init(self):
        list = List()

        self.assertEqual(str(list), '[]')
        self.assertEqual(len(list), 0)


class TestListAppend(unittest.TestCase):

    def setUp(self):
        self.list1 = List([1, 2, 3])
        self.list2 = List()

    def test_append_one_obejct(self):
        self.list1.append('test')
        self.list2.append({'test': 'well'})

        self.assertEqual(str(self.list1), "[1, 2, 3, test]")
        self.assertEqual(len(self.list1), 4)
        self.assertEqual(str(self.list2), "[{'test': 'well'}]")
        self.assertEqual(len(self.list2), 1)

        self.list1.append([6, 5, 4])
        self.assertEqual(str(self.list1), '[1, 2, 3, test, [6, 5, 4]]')
        self.assertEqual(len(self.list1), 5)

    def test_append_list(self):
        self.list1.append([1, 2, 3, 4])
        self.assertEqual(str(self.list1), "[1, 2, 3, [1, 2, 3, 4]]")
        self.assertEqual(len(self.list1), 4)

        self.list1.append(List([1, 2]))
        self.assertEqual(str(self.list1), "[1, 2, 3, [1, 2, 3, 4], [1, 2]]")
        self.assertEqual(len(self.list1), 5)

        self.list2.append(List())
        self.assertEqual(str(self.list2), "[[]]")
        self.assertEqual(len(self.list2), 1)


class TestListPop(unittest.TestCase):

    def setUp(self):
        self.list = List([1, 2, 3])

    def test_pop(self):
        data = self.list.pop()

        self.assertEqual(data, 3)
        self.assertEqual(str(self.list), '[1, 2]')
        self.assertEqual(len(self.list), 2)

    def test_pop_last(self):
        self.list.pop()
        self.list.pop()
        data = self.list.pop()

        self.assertEqual(data, 1)
        self.assertEqual(str(self.list), '[]')
        self.assertEqual(len(self.list), 0)

    def test_pop_from_empty_list(self):
        list1 = List()
        data = list1.pop()
        self.assertEqual(data, None)
        self.assertEqual(str(list1), '[]')
        self.assertEqual(len(list1), 0)


class TestListInsert(unittest.TestCase):

    def setUp(self):
        self.list = List([1, 2, 3, 4])
        self.list1 = List()

    def test_insert(self):
        self.list.insert('test', 1)
        self.assertEqual(str(self.list), '[1, test, 2, 3, 4]')
        self.assertEqual(len(self.list), 5)

        self.list.insert('test1', 0)
        self.assertEqual(str(self.list), '[test1, 1, test, 2, 3, 4]')
        self.assertEqual(len(self.list), 6)

        self.list.insert('test2', 6)
        self.assertEqual(str(self.list), '[test1, 1, test, 2, 3, 4, test2]')
        self.assertEqual(len(self.list), 7)

        self.list1.insert('well', 0)
        self.assertEqual(str(self.list1), '[well]')
        self.assertEqual(len(self.list1), 1)

    def test_exseptions(self):
        with self.assertRaises(ValueError):
            self.list.insert('well', 'good')
        with self.assertRaises(IndexError):
            self.list.insert('well', -1)
        with self.assertRaises(IndexError):
            self.list.insert('well', 10)


class TestListGetitem(unittest.TestCase):
    def test_get_by_positive_index(self):
        list = List([1, 2, 3])

        self.assertEqual(list[0], 1)
        self.assertEqual(list[2], 3)
        with self.assertRaises(IndexError):
            list[6]
        with self.assertRaises(IndexError):
            list[-1]
        with self.assertRaises(IndexError):
            List()[0]


class TestListReverse(unittest.TestCase):
    def test_get_reverse(self):
        list = List([1, 2, 3])
        temp = list.reverse()

        self.assertEqual(str(list), '[1, 2, 3]')
        self.assertEqual(str(temp), '[3, 2, 1]')
        self.assertEqual(len(temp), 3)
        self.assertEqual(len(list), 3)

        list1 = List()
        temp = list1.reverse()

        self.assertEqual(str(temp), '[]')
        self.assertEqual(len(temp), 0)


class TestListExtends(unittest.TestCase):
    def setUp(self):
        self.list1 = List()
        self.list2 = List([1, 2, 3])

    def test_add_default_list(self):
        self.list2.extend([4, 5, 6])
        self.assertEqual(str(self.list2), '[1, 2, 3, 4, 5, 6]')
        self.assertEqual(len(self.list2), 6)

        self.list1.extend([])
        self.assertEqual(str(self.list1), '[]')
        self.assertEqual(len(self.list1), 0)

        self.list1.extend([1, 2, 3])
        self.assertEqual(str(self.list1), '[1, 2, 3]')
        self.assertEqual(len(self.list1), 3)

        self.list1.extend([])
        self.assertEqual(str(self.list1), '[1, 2, 3]')
        self.assertEqual(len(self.list1), 3)

    def test_add_List(self):
        self.list1.extend(List([]))
        self.assertEqual(str(self.list1), '[]')
        self.assertEqual(len(self.list1), 0)

        self.list1.extend(self.list2)
        self.assertEqual(str(self.list1), '[1, 2, 3]')
        self.assertEqual(len(self.list1), 3)
        self.assertEqual(str(self.list2), '[1, 2, 3]')
        self.assertEqual(len(self.list2), 3)

        self.list2.extend(self.list2)
        self.assertEqual(str(self.list2), '[1, 2, 3, 1, 2, 3]')
        self.assertEqual(len(self.list2), 6)

        self.list1.extend(self.list2)
        self.assertEqual(str(self.list1), '[1, 2, 3, 1, 2, 3, 1, 2, 3]')
        self.assertEqual(len(self.list1), 9)

    def test_exception(self):
        with self.assertRaises(TypeError):
            self.list2.extend(34)


class TestListAdd(unittest.TestCase):
    def test_add(self):
        list = List()
        list = list + 1
        self.assertEqual(str(list), '[1]')
        self.assertEqual(len(list), 1)

        temp = list + List()
        self.assertEqual(str(temp), '[1, []]')
        self.assertEqual(str(list), '[1]')
        self.assertEqual(len(temp), 2)

        temp = list + {1: 2}
        self.assertEqual(str(temp), '[1, {1: 2}]')
        self.assertEqual(len(temp), 2)


if __name__ == '__main__':
    unittest.main()
