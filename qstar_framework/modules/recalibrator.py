# qstar/modules/recalibrator.py
def recalibrer_resultat(y, valid):
    if valid:
        return y
    return y + 1 if isinstance(y, (int, float)) else y[::-1]
