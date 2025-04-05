# qstar/edge/qstar_edge.py
import onnxruntime as ort
from transformers import AutoTokenizer


class QStarEdgeONNX:
    def __init__(
        self,
        model_path="onnx/qstar_model.onnx",
        tokenizer_name="distilbert-base-uncased",
    ):
        self.session = ort.InferenceSession(
            model_path, providers=["CPUExecutionProvider"]
        )
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def infer(self, text):
        inputs = self.tokenizer(text, return_tensors="np")
        ort_inputs = {k: v for k, v in inputs.items()}
        ort_outputs = self.session.run(None, ort_inputs)
        return ort_outputs[0]


if __name__ == "__main__":
    engine = QStarEdgeONNX()
    output = engine.infer("Q-STAR fonctionne sur les systèmes embarqués !")
    print("📦 Résultat ONNX :", output)
