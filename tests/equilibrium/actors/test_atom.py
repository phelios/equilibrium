from unittest import TestCase
from unittest.mock import patch

from equilibrium.actors.atom import Atom


class TestBaseCasee(TestCase):

    @patch('equilibrium.actors.atom.randint')
    def test_on_update(self, mock_randint):
        mock_randint.return_value = 1
        test_actor = Atom("Rando")
        test_actor.update()

        self.assertEqual(test_actor.x, 1)
        self.assertEqual(test_actor.y, 1)

    def test_random(self):
        from random import randint

        results = {}

        rng = (-1, 1)

        for x in range(rng[0], rng[1] + 1):
            results[x] = 0

        # self.assertEqual(results, {})

        for x in range(1000):
            results[randint(*rng)] += 1

        self.assertEqual(results, {})
