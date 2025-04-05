from fastapi import FastAPI, Request
from pydantic import BaseModel
from qstar.reinforcement.reward_fn import composite_reward
from qstar.reinforcement.train_rlhf import reward_fn
import logging

app = FastAPI(title="Q-STAR API")

class PromptInput(BaseModel):
    prompt: str
    response: str

@app.post("/reward")
def compute_reward(data: PromptInput):
    score = composite_reward(data.prompt, data.response)
    return {"reward": score}

@app.get("/ping")
def ping():
    return {"message": "Q-STAR API is alive"}

# Endpoint pour futurs modules : vision, NLP, multimodal
@app.post("/rlhf/step")
def simulate_rl_step(data: PromptInput):
    reward = reward_fn(data.prompt, data.response)
    return {
        "prompt": data.prompt,
        "response": data.response,
        "reward": reward
    }
