# qstar/async_core.py
import asyncio
from qstar.modules.processing import traitement_initial
from qstar.modules.verifier import verifier_output
from qstar.modules.recalibrator import recalibrer_resultat
from qstar.modules.correlate import corriger_par_correlation
from qstar.modules.synthesize import produire_resultat_final


class AsyncQStarPipeline:
    def __init__(self):
        self.logs = []

    async def run(self, input_data):
        y1 = await asyncio.to_thread(traitement_initial, input_data)
        self.logs.append(f"Initial: {y1}")

        is_valid = await asyncio.to_thread(verifier_output, input_data, y1)
        self.logs.append(f"Verification: {is_valid}")

        y2 = await asyncio.to_thread(recalibrer_resultat, y1, is_valid)
        self.logs.append(f"Recalibré: {y2}")

        y_corr = await asyncio.to_thread(corriger_par_correlation, input_data, y2)
        self.logs.append(f"Corrélé: {y_corr}")

        y_final = await asyncio.to_thread(produire_resultat_final, y_corr)
        self.logs.append(f"Final: {y_final}")

        return y_final

    def get_logs(self):
        return self.logs
