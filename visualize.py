import matplotlib.pyplot as plt
import numpy as np

def plot_training_rewards(rewards, save_path="outputs/training_rewards.png"):
    plt.figure()
    plt.plot(rewards)
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("Training Rewards Over Time")
    plt.savefig(save_path)
    plt.close()

def plot_trajectory(grid_size, obstacles, trajectory, goal, save_path="outputs/trajectory_plot.png"):
    grid = np.zeros((grid_size, grid_size))

    for obs in obstacles:
        grid[obs] = -1

    for step in trajectory:
        grid[step] = 0.5

    grid[goal] = 1

    plt.figure()
    plt.imshow(grid)
    plt.title("Agent Trajectory Through Warehouse GridWorld")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.savefig(save_path)
    plt.close()