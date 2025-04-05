# tools/benchmark.py
import time
from qstar.models.jax_module import QStarJAX
from qstar.models.tf_module import QStarTF
from qstar.models.llm_interface import QStarLLM

text = "La technologie Q-STAR optimise le raisonnement algorithmique."

start = time.time()
_ = QStarLLM().qstar_wrap(text)
print("[Benchmark] LLM (PyTorch):", round(time.time() - start, 4), "s")

start = time.time()
_ = QStarTF().qstar_tf_pipeline(text)
print("[Benchmark] TensorFlow:", round(time.time() - start, 4), "s")

start = time.time()
_ = QStarJAX().qstar_jax_pipeline(text)
print("[Benchmark] JAX:", round(time.time() - start, 4), "s")
