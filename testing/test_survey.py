from IPython import embed
import unittest
from survey import Survey

class TestSurvey(unittest.TestCase):
    """Test for the class Survey."""

    def setUp(self):
        """Setting up survey and responses to keep shit DRY."""
        question = "What games do you remember playing?"
        self.survey = Survey(question)
        self.responses = ['Contra', 'Rastan', 'Shinobi']

    def test_store_single_response(self):
        """Test that a single response is recorded properly."""
        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)

    def test_store_three_responses(self):
        """Tests that 3 individual responses are stored properly."""
        for response in self.responses:
            self.survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)

if __name__ == '__main__':
    unittest.main()
