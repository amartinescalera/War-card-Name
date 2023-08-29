# -*- coding: utf-8 -*-

from .context import war_card_game

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(war_card_game.hmm())


if __name__ == '__main__':
    unittest.main()
