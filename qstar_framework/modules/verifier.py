# qstar/modules/verifier.py
def verifier_output(x, y):
    return (x == y) if isinstance(x, str) else (abs(x - y) % 2 == 0)
