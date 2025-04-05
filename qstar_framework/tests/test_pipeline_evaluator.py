# tests/test_pipeline.py
import unittest
from qstar.qstar_core import QStarPipeline

class TestQStarPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = QStarPipeline()

    def test_text_input(self):
        result = self.pipeline.run("Bonjour Q-STAR")
        self.assertTrue(isinstance(result, str))

    def test_numeric_input(self):
        result = self.pipeline.run(42)
        self.assertTrue(isinstance(result, (int, float, str)))

    def test_logs_generated(self):
        self.pipeline.run("test")
        logs = self.pipeline.get_logs()
        self.assertGreaterEqual(len(logs), 5)

if __name__ == '__main__':
    unittest.main()
