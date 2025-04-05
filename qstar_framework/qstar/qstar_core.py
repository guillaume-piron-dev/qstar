# qstar/core.py
from qstar.modules.processing import traitement_initial
from qstar.modules.verifier import verifier_output
from qstar.modules.recalibrator import recalibrer_resultat
from qstar.modules.correlate import corriger_par_correlation
from qstar.modules.synthesize import produire_resultat_final


class QStarPipeline:
    def __init__(self):
        self.logs = []

    def run(self, input_data):
        # Étape 1 : Traitement initial
        y1 = traitement_initial(input_data)
        self.logs.append(f"[Étape 1] Initial : {y1}")

        # Étape 2 : Vérification asynchrone
        is_valid = verifier_output(input_data, y1)
        self.logs.append(f"[Étape 2] Vérification : {is_valid}")

        # Étape 3 : Recalibrage
        y2 = recalibrer_resultat(y1, is_valid)
        self.logs.append(f"[Étape 3] Recalibré : {y2}")

        # Étape 4 : Corrélation
        y_corr = corriger_par_correlation(input_data, y2)
        self.logs.append(f"[Étape 4] Corrélé : {y_corr}")

        # Étape 5 : Synthèse finale
        y_final = produire_resultat_final(y_corr)
        self.logs.append(f"[Étape 5] Final : {y_final}")

        return y_final

    def get_logs(self):
        return self.logs
