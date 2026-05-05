# evaluate.py
from environment import WarehouseGridWorld
from agent import QAgent
from text_encoder import encode_command
from collections import defaultdict
import numpy as np
import pickle

env = WarehouseGridWorld()
agent = QAgent()

# Load trained Q-table BEFORE evaluation
with open("outputs/q_table.pkl", "rb") as f:
    loaded_q = pickle.load(f)

agent.q_table = defaultdict(lambda: np.zeros(4), loaded_q)

command = "go to shelf b3"
goal = encode_command(command)
env.goal = goal

state, _ = env.reset()
state = tuple(state)

done = False
steps = 0
max_steps = 50

print(f"AI received command: '{command}'")
print(f"Goal location: {goal}")

while not done and steps < max_steps:
    action = np.argmax(agent.q_table[state])

    next_state, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
    state = tuple(next_state)

    steps += 1
    print(f"Step {steps}: {state}, Action: {action}, Reward: {reward}")

if done:
    print("Destination reached!")
else:
    print("Agent did not reach destination within max steps.")

print("Total steps:", steps)