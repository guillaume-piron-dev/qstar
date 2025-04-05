# qstar/modules/correlate.py
def corriger_par_correlation(x, y):
    if isinstance(y, (int, float)):
        return y + (0.1 if x < y else -0.1)
    return y.lower() if isinstance(y, str) else y
