import unittest
from qstar.qstar_core import QStarPipeline


class TestQStarPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = QStarPipeline()

    def test_numeric_input(self):
        """Teste si un entier donné produit une chaîne cohérente contenant le chiffre."""
        result = self.pipeline.run(10)
        self.assertIsInstance(result, str)
        self.assertIn("10", result)  # ✅ On attend une mention directe

    def test_string_input(self):
        """Teste une entrée textuelle simple."""
        input_str = "test"
        result = self.pipeline.run(input_str)
        self.assertIsInstance(result, str)
        self.assertIn(input_str, result.lower())  # 🔍 Validation souple

    def test_pipeline_logs(self):
        """Vérifie que les logs contiennent bien les mentions de traitement initial."""
        self.pipeline.run("debug")
        logs = self.pipeline.get_logs()
        self.assertIsInstance(logs, list)
        self.assertTrue(any("initial" in log.lower() for log in logs))  # 🔍 Cohérence sémantique

if __name__ == '__main__':
    unittest.main()
