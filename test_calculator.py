# Unittest for simple calculator
# author: Muztrizen

import unittest
import calculator


class TestCalculator(unittest.TestCase):

  def test_add(self):
    """
    Test case: Normal case of addition
    """
    expected_answer = 1
    actual_answer = calculator.add(1, 0)
    self.assertEqual(expected_answer, actual_answer)

  def test_subtract(self):
    """
    Test case: Normal case of subtraction
    """
    expected_answer = 1
    actual_answer = calculator.subtract(2, 1)
    self.assertEqual(expected_answer, actual_answer)

  def test_multiply(self):
    """
    Test case:  Normal case of multiplication
    """
    expected_answer = 1
    actual_answer = calculator.multiply(1, 1)
    self.assertEqual(expected_answer, actual_answer)

  def test_divide(self):
    """
    Test case:  Normal case of division
    """
    expected_answer = 1
    actual_answer = calculator.divide(2, 2)
    self.assertEqual(expected_answer, actual_answer)

    """
    Test case: Raise ValueError when y ==0
    """
    with self.assertRaises(ValueError):
      calculator.divide(1, 0)
