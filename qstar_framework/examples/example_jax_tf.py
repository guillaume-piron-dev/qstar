# examples/example_jax_tf.py
from qstar.models.jax_module import QStarJAX
from qstar.models.tf_module import QStarTF

text_input = "Q-STAR est une avancée dans la vérification des IA."

# JAX Example
jax_model = QStarJAX()
jax_result = jax_model.qstar_jax_pipeline(text_input)
print("[JAX] Résultat final:", jax_result)

# TensorFlow Example
tf_model = QStarTF()
tf_result = tf_model.qstar_tf_pipeline(text_input)
print("[TensorFlow] Résultat final:", tf_result)
