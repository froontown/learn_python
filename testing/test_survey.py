import unittest
from survey import Survey

class TestSurvey(unittest.TestCase):
    """Test for the class Survey."""

    def test_store_single_response(self):
        """Test that a single response is recorded properly."""
        question = "What games do you remember playing?"
        my_survey = Survey(question)
        my_survey.store_response('Contra')
        self.assertIn('Contra', my_survey.responses)

    def test_store_three_responses(self):
        """Tests that 3 individual responses are stored properly."""
        q = "What games do you remember playing?"
        survey = Survey(q)
        responses = ['Contra', 'Rastan', "Shinobi"]
        for response in responses:
            survey.store_response(response)
        for response in responses:
            self.assertIn(response, survey.responses)

if __name__ == '__main__':
    unittest.main()
