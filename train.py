# train.py
from environment import WarehouseGridWorld
from agent import QAgent
from text_encoder import encode_command
from visualize import plot_training_rewards
import numpy as np
import os
import pickle

env = WarehouseGridWorld()
agent = QAgent()

alpha = 0.1
gamma = 0.9
epsilon = 1.0
epsilon_decay = 0.995
episodes = 3000

commands = [
    "go to shelf b3"
]

reward_history = []

os.makedirs("outputs", exist_ok=True)

for ep in range(episodes):
    command = np.random.choice(commands)
    goal = encode_command(command)
    env.goal = goal

    state, _ = env.reset()
    state = tuple(state)

    done = False
    total_reward = 0
    steps = 0

    while not done:
        action = agent.choose_action(state, epsilon)

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        next_state = tuple(next_state)

        agent.update(state, action, reward, next_state, alpha, gamma)

        state = next_state
        total_reward += reward
        steps += 1

    reward_history.append(total_reward)
    epsilon *= epsilon_decay

    if (ep + 1) % 250 == 0:
        print(
            f"Episode {ep + 1}: "
            f"Command='{command}', "
            f"Goal={goal}, "
            f"Steps={steps}, "
            f"Total Reward={total_reward}, "
            f"Epsilon={epsilon:.3f}"
        )

with open("outputs/q_table.pkl", "wb") as f:
    pickle.dump(dict(agent.q_table), f)

plot_training_rewards(reward_history)

print("Training complete. Q-table saved to outputs/q_table.pkl")
print("Training reward plot saved to outputs/training_rewards.png")