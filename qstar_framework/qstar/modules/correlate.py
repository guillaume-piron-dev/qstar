import difflib


def corriger_par_correlation(input_text, recalibrated_text):
    # 🔒 Patch ici pour éviter erreur si int est passé
    input_text = str(input_text)
    recalibrated_text = str(recalibrated_text)

    ratio = difflib.SequenceMatcher(None, input_text, recalibrated_text).ratio()
    if ratio > 0.8:
        return recalibrated_text
    return input_text + " / " + recalibrated_text
