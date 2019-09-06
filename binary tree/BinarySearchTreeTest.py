from tree import BinarySearchTree
import unittest


class TestBinarySearchTreeInit(unittest.TestCase):
    def test_dict_with_one_value(self):
        tree1 = BinarySearchTree({1: 'str'})
        self.assertEqual(str(tree1), '{1: str}')
        self.assertEqual(len(tree1), 1)

        tree2 = BinarySearchTree({54: [32, {'well': 32}]})
        self.assertEqual(str(tree2), "{54: [32, {'well': 32}]}")
        self.assertEqual(len(tree2), 1)

        with self.assertRaises(TypeError):
            tree3 = BinarySearchTree({'1': 'well'})

        with self.assertRaises(TypeError):
            tree3 = BinarySearchTree('hello')

        tree3 = BinarySearchTree()
        self.assertEqual(str(tree3), "{}")
        self.assertEqual(len(tree3), 0)

        with self.assertRaises(TypeError):
            tree4 = BinarySearchTree({})

    def test_dict_with_some_values(self):
        tree1 = BinarySearchTree({1: 'test', 43: 'well', 23: 'good'})
        self.assertEqual(str(tree1), "{1: test, 23: good, 43: well}")
        self.assertEqual(len(tree1), 3)

        with self.assertRaises(TypeError):
            tree2 = BinarySearchTree({'1': 4, 2: 'well'})

        with self.assertRaises(TypeError):
            tree2 = BinarySearchTree({1: 4, '2': 'well', 3: 'hello'})


class TestBinarySearchTreeAppend(unittest.TestCase):
    def setUp(self):
        self.tree1 = BinarySearchTree({1: 'well'})
        self.tree2 = BinarySearchTree()

    def test_append_one_value(self):
        self.tree1.append({2: 'test'})
        self.assertEqual(str(self.tree1), "{1: well, 2: test}")
        self.assertEqual(len(self.tree1), 2)

        self.tree1.append({-1: 'new'})
        self.assertEqual(str(self.tree1), "{-1: new, 1: well, 2: test}")
        self.assertEqual(len(self.tree1), 3)

        with self.assertRaises(TypeError):
            self.tree1.append(2)

        with self.assertRaises(TypeError):
            self.tree1.append({'2': 32})

        with self.assertRaises(TypeError):
            self.tree2.append(2)

        with self.assertRaises(TypeError):
            self.tree2.append({'2': 32})

        self.tree2.append({-3: 4})
        self.assertEqual(str(self.tree2), "{-3: 4}")
        self.assertEqual(len(self.tree2), 1)

        with self.assertRaises(ValueError):
            self.tree2.append({-3: '23'})

        with self.assertRaises(ValueError):
            self.tree1.append({2: '23'})

    def test_append_some_values(self):
        self.tree1.append({2: 'test', -1: 'new'})
        self.assertEqual(str(self.tree1), "{-1: new, 1: well, 2: test}")
        self.assertEqual(len(self.tree1), 3)

        with self.assertRaises(TypeError):
            self.tree1.append({1: 3, '2': 32})

        with self.assertRaises(TypeError):
            self.tree1.append({'1': 3, 2: 32})

        with self.assertRaises(TypeError):
            self.tree2.append({3: 31, '2': 32})

        self.tree2.append({-3: 4, 1: 4})
        self.assertEqual(str(self.tree2), "{-3: 4, 1: 4}")
        self.assertEqual(len(self.tree2), 2)

        with self.assertRaises(ValueError):
            self.tree2.append({32: 'h', -3: '23'})


class TestBinarySearchTreeGet(unittest.TestCase):
    def test_get(self):
        tree1 = BinarySearchTree({4: 'well', 1: 'test', 7: 'good'})
        temp = tree1.get(1)
        temp1 = tree1[1]
        self.assertEqual(str(temp), 'test')
        self.assertEqual(str(temp1), 'test')

        temp = tree1.get(7)
        temp1 = tree1[7]
        self.assertEqual(str(temp), 'good')
        self.assertEqual(str(temp1), 'good')

        temp = tree1.get(4)
        temp1 = tree1[4]
        self.assertEqual(str(temp), 'well')
        self.assertEqual(str(temp1), 'well')

        tree2 = BinarySearchTree()
        with self.assertRaises(KeyError):
            tree2.get(1)

        with self.assertRaises(KeyError):
            tree2[1]

        with self.assertRaises(KeyError):
            tree1.get(8)

        with self.assertRaises(KeyError):
            tree1[8]


class TestBinarySearchTreeErase(unittest.TestCase):
    def test_erase_node_with_to_children(self):
        tree = BinarySearchTree({4: 'a', 2: 'b', 3: 'c', 1: 'd'})
        tree.erase(2)
        self.assertEqual(str(tree), '{1: d, 3: c, 4: a}')
        self.assertEqual(len(tree), 3)
        tree1 = BinarySearchTree({4: 'a', 2: 'b', 3: 'c', 1: 'd', -2: 'e'})
        tree1.erase(2)
        self.assertEqual(str(tree1), '{-2: e, 1: d, 3: c, 4: a}')
        self.assertEqual(len(tree1), 4)

        tree2 = BinarySearchTree({-10: 'a', 2: 'b', 3: 'c', 1: 'd'})
        tree2.erase(2)
        self.assertEqual(str(tree2), '{-10: a, 1: d, 3: c}')
        self.assertEqual(len(tree2), 3)

        tree3 = BinarySearchTree({-10: 'a', 2: 'b', 3: 'c', 1: 'd', -4: 'e'})
        tree3.erase(2)
        self.assertEqual(str(tree3), '{-10: a, -4: e, 1: d, 3: c}')
        self.assertEqual(len(tree3), 4)

        tree4 = BinarySearchTree({-10: 'a', 2: 'b', 3: 'c', 1: 'd', -4: 'e'})
        tree4.erase(-10)
        self.assertEqual(str(tree4), '{-4: e, 1: d, 2: b, 3: c}')
        self.assertEqual(len(tree4), 4)

    def test_erase_node_without_children(self):
        tree = BinarySearchTree({1: 'a'})
        tree.erase(1)
        self.assertEqual(str(tree), '{}')
        self.assertEqual(len(tree), 0)

        tree1 = BinarySearchTree({2: 'a', 1: 'b', 3: 'c'})
        tree1.erase(1)
        self.assertEqual(str(tree1), '{2: a, 3: c}')
        self.assertEqual(len(tree1), 2)

        tree1.erase(3)
        self.assertEqual(str(tree1), '{2: a}')
        self.assertEqual(len(tree1), 1)

    def test_erase_node_with_one_child(self):
        tree = BinarySearchTree({1: 'a', 2: 'b'})
        tree.erase(1)
        self.assertEqual(str(tree), '{2: b}')
        self.assertEqual(len(tree), 1)

        tree1 = BinarySearchTree({1: 'a', 2: 'b', 5: 'c', 4: 'd', 6: 'e'})
        tree1.erase(2)
        self.assertEqual(str(tree1), '{1: a, 4: d, 5: c, 6: e}')
        self.assertEqual(len(tree1), 4)

    def test_exceptions(self):
        tree = BinarySearchTree()
        with self.assertRaises(ValueError):
            tree.erase(3)

        tree1 = BinarySearchTree({1: 2})
        with self.assertRaises(TypeError):
            tree.erase('3')

        with self.assertRaises(ValueError):
            tree1.erase(3)


if __name__ == '__main__':
    unittest.main()
