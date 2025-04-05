# qstar/core/interop/tf_adapter.py
import tensorflow as tf


class TensorFlowAdapter:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, input_data):
        return self.model.predict(input_data)

    def summary(self):
        return self.model.summary()


if __name__ == "__main__":
    adapter = TensorFlowAdapter("./saved_model")
    adapter.summary()
