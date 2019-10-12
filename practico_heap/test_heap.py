import unittest
import random

from heap import Heap


class ConstructorTestCase(unittest.TestCase):
    def test_constructor_does_not_accept_parameters(self):
        with self.assertRaises(TypeError):
            Heap(1)
            Heap(1, 2)


class IsEmptyTestCase(unittest.TestCase):
    def test_new_heap_is_empty(self):
        h = Heap()
        self.assertTrue(h.is_empty())

    def test_heap_with_one_element_is_not_empty(self):
        h = Heap()
        h.enqueue(1)
        self.assertFalse(h.is_empty())

    def test_heap_with_many_elements_is_not_empty(self):
        h = Heap()
        for i in range(10):
            h.enqueue(i)
        self.assertFalse(h.is_empty())

    def test_enqueue_one_and_dequeue_one(self):
        h = Heap()
        h.enqueue(19)
        h.dequeue()
        self.assertTrue(h.is_empty())

    def test_enqueue_many_and_dequeue_equal_amount(self):
        h = Heap()
        top = 10
        for _ in range(top):
            h.enqueue(1)

        for _ in range(top):
            h.dequeue()
        self.assertTrue(h.is_empty())


class PrioritiesTestCase(unittest.TestCase):
    def test_dequeue_ordering(self):
        # enqueue a bunch of elements and dequeue them, expecting to get elements in reversed order
        cases = (
            (),
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
            (1, 1, 2),
            (1, 2, 1),
            (2, 1, 1),
            (2, 1, 1, 4),
            (2, 1, 1, 4, -1, 12, 123),
        )
        for case in cases:
            with self.subTest(case):
                h = Heap()
                for elem in case:
                    h.enqueue(elem)
                retrieved = []
                while not h.is_empty():
                    retrieved.append(h.dequeue())
                self.assertEqual(retrieved, sorted(case, reverse=True))

    def test_dequeue_ordering_random_elements(self):
        for _ in range(10):
            data = [random.randint(-100, 100) for _ in range(20)]
            with self.subTest(data):
                h = Heap()
                for elem in data:
                    h.enqueue(elem)
                retrieved = []
                while not h.is_empty():
                    retrieved.append(h.dequeue())
                self.assertEqual(retrieved, sorted(data, reverse=True))
