import unittest
from IPython import embed
from exercise2 import Employee

class TestEmployee(unittest.TestCase):
    """Testing giving the employees a custom raise and a default raise."""

    def setUp(self):
        """Setting up instances for the tests."""
        self.employee = Employee('Francis', 'Kim', 5000000)

    def test_default_raise(self):
        """Test that a default raise can be given."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 5005000)

    def test_custom_raise(self):
        """Test a custom raise, yo"""
        self.employee.give_raise(5000000)
        self.assertEqual(self.employee.salary, 10000000)
