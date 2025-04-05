import gradio as gr
from qstar.reinforcement.reward_fn import composite_reward

def evaluate_qstar(prompt, response):
    score = composite_reward(prompt, response)
    return f"Score Q-STAR : {score:.3f}"

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Q-STAR – Évaluation asynchrone intelligente")

    with gr.Row():
        prompt_input = gr.Textbox(label="Prompt utilisateur", placeholder="...")
        response_input = gr.Textbox(label="Réponse du modèle", placeholder="...")

    submit_btn = gr.Button("Évaluer")
    output_score = gr.Textbox(label="Score", interactive=False)

    submit_btn.click(fn=evaluate_qstar, inputs=[prompt_input, response_input], outputs=output_score)

demo.launch()
