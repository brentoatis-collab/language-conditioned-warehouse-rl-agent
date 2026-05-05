# agent.py
from collections import defaultdict
import numpy as np

class QAgent:
    def __init__(self):
        self.q_table = defaultdict(lambda: np.zeros(4))

    def choose_action(self, state, epsilon):
        if np.random.rand() < epsilon:
            return np.random.randint(4)
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state, alpha, gamma):
        best_next = np.max(self.q_table[next_state])
        self.q_table[state][action] += alpha * (reward + gamma * best_next - self.q_table[state][action])