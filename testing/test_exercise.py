import unittest
from exercise import city

class CityTest(unittest.TestCase):
    """Tests the city address punctuation."""

    def test_city(self):
        """Checks the formatting of the cityname."""
        the_city = city('dover', 'massachusetts')
        self.assertEqual(the_city, 'Dover, Massachusetts')

    def test_population(self):
        """Checks if there is a population."""
        the_city = city('dover', 'massachusetts', 200)
        self.assertEqual(the_city, 'Dover, Massachusetts - 200')

if __name__ == '__main__':
    unittest.main()
