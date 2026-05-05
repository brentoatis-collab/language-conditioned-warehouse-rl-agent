# RL + NLP GridWorld Agent  
### Language-Conditioned Reinforcement Learning for Warehouse Navigation

---

## Overview

This project implements a **language-conditioned reinforcement learning (RL) agent** capable of interpreting natural language commands and executing navigation tasks within a GridWorld environment.

The system simulates a **smart warehouse robot** that receives instructions such as:

> *“Go to shelf B3”*

and translates them into optimal movement decisions using Q-learning.

---

## Objective

To demonstrate how **Natural Language Processing (NLP)** and **Reinforcement Learning (RL)** can be integrated to create adaptive systems that:

- Understand human language
- Convert instructions into actionable goals
- Learn optimal navigation policies through experience
- Improve efficiency over time

---

## System Architecture

Text Command -> Text Encoder -> RL Agent -> DridWorld Environment

### Components:

- **Text Encoder**
  - Converts commands (e.g., "B3") → grid coordinates (1,2)

- **GridWorld Environment**
  - 5x5 warehouse layout
  - Obstacles and movement constraints
  - Reward-based navigation system

- **Q-Learning Agent**
  - Learns optimal actions using state-action values
  - Uses epsilon-greedy exploration strategy

---

## Technologies Used

- Python
- NumPy
- Gymnasium
- Matplotlib

---

## Project Structure

CST643_Week7_RL_NLP_agent

- environment.py
- text_encoder.py
- agent.py
- train.py
- evaluate.py
- visualize.py
- requirements.txt
- claude_log.md
- README.md
- .gitignore
- outputs/
    - q_table.pkl
    - training_rewards.png

## Installation

### 1. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Train the Agent

```bash
python3 train.py
```

This will:
- Train the RL agent
- Save Q-table → `outputs/q_table.pkl`
- Generate reward graph → `outputs/training_rewards.png`

---

### Evaluate the Agent

```bash
python3 evaluate.py
```

Example output:
AI received command: 'go to shelf b3'
Goal location: (1, 2)
Step 1: (0, 1)
Step 2: (1, 1)
Step 3: (1, 2)
Destination reached!
Total steps: 3

---

## Results

- **Success Rate:** High (consistent goal completion)
- **Average Steps:** ~3 steps to reach target
- **Learning Behavior:** Reward convergence observed

### Training Reward Curve

![Training Rewards](outputs/training_rewards.png)

---

## Key Insights

- RL enables agents to learn optimal navigation strategies through trial and error.
- NLP allows dynamic task definition through natural language.
- Combining both enables **generalized behavior across instructions**, not fixed policies.

> A traditional RL agent learns *what to do*.  
> A language-conditioned RL agent learns *what to do based on what it is told*.

---

## Challenges Encountered

| Challenge | Solution |
|----------|--------|
| Infinite evaluation loops | Added max step constraint |
| Q-table not loading | Ensured proper load before evaluation |
| Policy instability | Simplified training to single command |
| Gym vs Gymnasium mismatch | Updated API handling |

---

## Future Improvements

- Replace rule-based encoder with embedding models (e.g., BERT)
- Introduce multiple simultaneous goals
- Expand GridWorld to larger environments
- Implement Deep Q-Network (DQN)

---

## References

Uc-Cetina, V., Navarro-Guerrero, N., Martin-Gonzalez, A., Weber, C., & Wermter, S. (2022).  
*Survey on reinforcement learning for language processing.* Artificial Intelligence Review.

GeeksforGeeks. (2025).  
*Q-learning in reinforcement learning.*  

IBM. (2025).  
*Natural language processing.*  

---

## Conclusion

This project demonstrates how integrating NLP with RL creates adaptive, intelligent systems capable of interpreting human intent and executing tasks efficiently.

It marks the transition from static automation to **context-aware decision-making systems**.