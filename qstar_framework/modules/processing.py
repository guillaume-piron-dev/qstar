# qstar/modules/processing.py
def traitement_initial(x):
    return x * 2 if isinstance(x, (int, float)) else str(x).upper()