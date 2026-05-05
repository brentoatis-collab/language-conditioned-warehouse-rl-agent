# environment.py
import numpy as np
import gymnasium as gym
from gymnasium import spaces


class WarehouseGridWorld(gym.Env):
    def __init__(self, grid_size=5):
        super().__init__()
        self.grid_size = grid_size
        self.start = (0, 0)
        self.state = self.start
        self.goal = (4, 4)

        self.obstacles = {(2, 1), (2, 3), (3, 1)}

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(
            low=0,
            high=grid_size - 1,
            shape=(2,),
            dtype=np.int32
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = self.start
        return np.array(self.state, dtype=np.int32), {}

    def step(self, action):
        x, y = self.state
        proposed_x, proposed_y = x, y

        if action == 0:
            proposed_x = max(x - 1, 0)
        elif action == 1:
            proposed_x = min(x + 1, self.grid_size - 1)
        elif action == 2:
            proposed_y = max(y - 1, 0)
        elif action == 3:
            proposed_y = min(y + 1, self.grid_size - 1)

        if (proposed_x, proposed_y) in self.obstacles:
            reward = -5
        else:
            self.state = (proposed_x, proposed_y)
            reward = -1

        if self.state == self.goal:
            reward = 10

        terminated = self.state == self.goal
        truncated = False

        return np.array(self.state, dtype=np.int32), reward, terminated, truncated, {}