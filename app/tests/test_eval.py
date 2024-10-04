import unittest
from eval import evaluate_response

class EvalTests(unittest.TestCase):

    def test_evaluate_response(self):
        generated_response = "This is a test response."
        reference_response = "This is a reference response."

        scores = evaluate_response(generated_response, reference_response)

        self.assertTrue(0 <= scores['F1'] <= 1, "F1 score is out of bounds")
        self.assertTrue(0 <= scores['P'] <= 1, "Precision score is out of bounds")
        self.assertTrue(0 <= scores['R'] <= 1, "Recall score is out of bounds")

if __name__ == '__main__':
    unittest.main()
