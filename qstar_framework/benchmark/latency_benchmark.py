# benchmark/latency_benchmark.py
import time
import torch
import transformers
import onnxruntime as ort
import jax
import tensorflow as tf
import numpy as np


def benchmark_pytorch(model_name, prompt):
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    model = transformers.AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    model.eval()
    with torch.no_grad():
        start = time.time()
        model(**inputs)
        end = time.time()
    return end - start


def benchmark_onnx(model_path, prompt, tokenizer_name):
    tokenizer = transformers.AutoTokenizer.from_pretrained(tokenizer_name)
    inputs = tokenizer(prompt, return_tensors="np")
    session = ort.InferenceSession(model_path)
    start = time.time()
    session.run(None, {k: v for k, v in inputs.items()})
    end = time.time()
    return end - start


def benchmark_tf(prompt):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(128,)),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1)
    ])
    dummy = np.random.rand(1, 128)
    start = time.time()
    model(dummy)
    end = time.time()
    return end - start


def benchmark_jax():
    x = jax.numpy.ones((1000, 1000))
    start = time.time()
    y = jax.numpy.dot(x, x).block_until_ready()
    end = time.time()
    return end - start


if __name__ == "__main__":
    prompt = "Décris le rôle de Q-STAR dans le traitement séquentiel."

    print("⏱️ Benchmark PyTorch:", benchmark_pytorch("distilgpt2", prompt), "sec")
    print("⏱️ Benchmark TensorFlow:", benchmark_tf(prompt), "sec")
    print("⏱️ Benchmark ONNX:", benchmark_onnx("onnx/qstar_model.onnx", prompt, "distilgpt2"), "sec")
    print("⏱️ Benchmark JAX:", benchmark_jax(), "sec")