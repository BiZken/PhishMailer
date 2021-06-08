import unittest
from Core.helper.date import monthName

class TestMonthName(unittest.TestCase):
  def test_normal(self):
    self.assertEqual(monthName(1), 'January')