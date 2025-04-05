# examples/example_edge.py
from qstar.edge.qstar_edge import QStarEdgeONNX

if __name__ == "__main__":
    print("⚙️ Exécution de Q-STAR en mode edge (ONNX)")

    edge_runner = QStarEdgeONNX()
    sentence = "L'inférence embarquée permet l'autonomie locale."
    output = edge_runner.infer(sentence)

    print("\n💻 Texte :", sentence)
    print("📊 Sortie ONNX :", output)
