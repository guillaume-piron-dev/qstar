# qstar/modules/verifier.py
from qstar.reinforcement.reward_fn import composite_reward


def verifier_output(input_data, output):
    score = composite_reward(input_data, output)
    return score >= 0.9
