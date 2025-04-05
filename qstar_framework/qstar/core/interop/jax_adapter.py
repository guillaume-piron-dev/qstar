# qstar/core/interop/jax_adapter.py
import jax
import jax.numpy as jnp


class JAXAdapter:
    def __init__(self):
        pass

    def compute(self, x):
        # Simple operation for demonstration
        return jax.jit(lambda x: x * x + 2)(x)

    def batched_compute(self, x):
        return jax.vmap(self.compute)(x)


if __name__ == "__main__":
    adapter = JAXAdapter()
    result = adapter.compute(jnp.array([3.0]))
    print("Résultat JAX:", result)
