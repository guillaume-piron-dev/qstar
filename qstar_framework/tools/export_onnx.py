# tools/export_onnx.py
import torch
from transformers import AutoTokenizer, AutoModel
import os

def export_to_onnx(model_name="bert-base-uncased", output_path="onnx_model"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    inputs = tokenizer("ONNX export sample", return_tensors="pt")
    os.makedirs(output_path, exist_ok=True)
    torch.onnx.export(
        model,
        (inputs["input_ids"],),
        f"{output_path}/{model_name.replace('/', '_')}.onnx",
        input_names=["input_ids"],
        output_names=["output"],
        dynamic_axes={"input_ids": {0: "batch_size"}, "output": {0: "batch_size"}},
        opset_version=11
    )
    print("ONNX exporté avec succès.")