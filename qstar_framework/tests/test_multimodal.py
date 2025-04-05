# tests/test_multimodal.py
import unittest
from qstar.models.multimodal_interface import QStarMultimodal

class TestQStarMultimodal(unittest.TestCase):
    def setUp(self):
        self.model = QStarMultimodal()

    def test_text_only(self):
        result = self.model.analyze(prompt="Bonjour le monde")
        self.assertIn("texte", result)
        self.assertTrue(len(result["texte"]) > 0)

    def test_invalid_inputs(self):
        result = self.model.analyze()
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
