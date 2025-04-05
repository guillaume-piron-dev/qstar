# agents/qstar_agent.py
from qstar.core import QStarPipeline

class QStarAgent:
    def __init__(self, name="AgentQ"):
        self.name = name
        self.pipeline = QStarPipeline()

    def interact(self, user_input):
        print(f"🤖 [{self.name}] Reçoit :", user_input)
        output = self.pipeline.run(user_input)
        print(f"✅ [{self.name}] Réponse :", output)
        return output

if __name__ == "__main__":
    agent = QStarAgent()
    while True:
        user_input = input("👤 Vous : ")
        if user_input.lower() in ["exit", "quit"]:
            break
        agent.interact(user_input)
