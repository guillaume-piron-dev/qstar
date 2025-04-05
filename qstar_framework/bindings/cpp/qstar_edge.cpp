# bindings/cpp/qstar_edge.cpp
#include <onnxruntime_cxx_api.h>
#include <iostream>
#include <vector>

int main() {
    Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "qstar");
    Ort::SessionOptions session_options;
    session_options.SetIntraOpNumThreads(1);
    Ort::Session session(env, "onnx_model/bert-base-uncased.onnx", session_options);
    std::cout << "[C++] Session ONNX Q-STAR initialisée avec succès." << std::endl;
    return 0;
}
