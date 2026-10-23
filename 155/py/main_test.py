import unittest

from main import MinStack


class TestMinStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = MinStack()

    def test_push_and_top(self) -> None:
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top(), 2)

    def test_push_and_pop(self) -> None:
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 1)

    def test_get_min_single(self) -> None:
        self.stack.push(5)
        self.assertEqual(self.stack.getMin(), 5)

    def test_get_min_after_pushes(self) -> None:
        self.stack.push(-2)
        self.stack.push(0)
        self.stack.push(-3)
        self.assertEqual(self.stack.getMin(), -3)

    def test_get_min_after_pop(self) -> None:
        self.stack.push(-2)
        self.stack.push(0)
        self.stack.push(-3)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), -2)

    def test_get_min_after_all_pops(self) -> None:
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.pop()
        # stack vacio: no se puede llamar getMin sin elementos
        # pero el problema garantiza que solo se llama con stack no-vacio

    def test_min_not_top(self) -> None:
        # el minimo puede ser distinto del top
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.top(), 2)
        self.assertEqual(self.stack.getMin(), 1)

    def test_leetcode_example(self) -> None:
        # MinStack, push(-2), push(0), push(-3), getMin=-3, pop, top=0, getMin=-2
        self.stack.push(-2)
        self.stack.push(0)
        self.stack.push(-3)
        self.assertEqual(self.stack.getMin(), -3)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 0)
        self.assertEqual(self.stack.getMin(), -2)

    def test_duplicate_min(self) -> None:
        # varios elementos con el mismo minimo
        self.stack.push(1)
        self.stack.push(1)
        self.stack.push(1)
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)

    def test_min_decreasing(self) -> None:
        # valores decrecientes
        self.stack.push(5)
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual(self.stack.getMin(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 4)

    def test_min_increasing(self) -> None:
        # valores crecientes: el minimo no cambia
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)

    def test_negatives_and_positives(self) -> None:
        self.stack.push(10)
        self.stack.push(-5)
        self.stack.push(20)
        self.stack.push(-10)
        self.assertEqual(self.stack.getMin(), -10)
        self.assertEqual(self.stack.top(), -10)

    def test_pop_to_smaller_min(self) -> None:
        # al hacer pop el nuevo minimo vuelve a ser el menor anterior
        self.stack.push(1)
        self.stack.push(5)
        self.stack.push(2)
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)

    def test_top_reflects_lifo(self) -> None:
        # el top refleja el orden LIFO
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.top(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 1)

    def test_large_values(self) -> None:
        self.stack.push(-1000000)
        self.stack.push(1000000)
        self.assertEqual(self.stack.getMin(), -1000000)
        self.assertEqual(self.stack.top(), 1000000)

    def test_interleaved_push_pop(self) -> None:
        s = self.stack
        s.push(3)
        s.push(5)
        s.push(1)
        s.push(4)
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.getMin(), 3)
        s.pop()
        self.assertEqual(s.getMin(), 3)

    def test_repeated_min_after_pop(self) -> None:
        # el minimo aparece multiples veces y persiste tras pops
        self.stack.push(0)
        self.stack.push(0)
        self.stack.push(-1)
        self.stack.push(-1)
        self.assertEqual(self.stack.getMin(), -1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), -1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 0)


if __name__ == "__main__":
    unittest.main()
