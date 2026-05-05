# Claude Code Conversation Log — Week 7 RL + NLP GridWorld Agent

## Project Overview
This project implements a language-conditioned reinforcement learning (RL) agent that interprets text-based commands and navigates a GridWorld warehouse environment. The system integrates natural language processing (NLP) with Q-learning to enable adaptive decision-making based on user instructions.

---

## System Architecture
The system consists of three primary components:

1. **Text Encoder Module**
   - Converts natural language commands (e.g., "go to shelf B3") into structured grid coordinates.
   - Provides the goal state for the RL agent.

2. **Warehouse GridWorld Environment**
   - A 5x5 grid representing a warehouse layout.
   - Includes obstacles, movement constraints, and a reward structure.
   - Defines states, actions, and transitions.

3. **Q-Learning Agent**
   - Uses an epsilon-greedy policy for exploration and exploitation.
   - Learns optimal navigation strategies through reward feedback.
   - Updates Q-values based on state transitions and rewards.

---

## Development Workflow (Vibe Coding Process)

### Step 1: System Planning
Defined the overall architecture before coding. Identified the need for modular components: environment, text encoder, agent, training loop, and evaluation.

---

### Step 2: Text Encoding Implementation
Developed a rule-based encoder to map shelf identifiers (A1–E5) to grid coordinates. This enabled the system to translate language into actionable goals.

---

### Step 3: Environment Design
Created a custom GridWorld using Gymnasium:
- Defined agent start position and goal state.
- Implemented obstacle handling.
- Designed a reward system:
  - +10 for reaching goal
  - -5 for hitting obstacles
  - -1 per step to encourage efficiency

---

### Step 4: RL Agent Development
Implemented a Q-learning agent:
- State-action value table using defaultdict
- Epsilon-greedy action selection
- Q-value update rule using learning rate and discount factor

---

### Step 5: Training Pipeline
Built the training loop:
- Sampled commands and updated environment goals dynamically
- Trained over multiple episodes
- Logged rewards and steps for performance tracking
- Applied epsilon decay to shift from exploration to exploitation

---

### Step 6: Evaluation and Debugging
Tested the trained agent using deterministic policy (argmax):
- Identified issue where Q-table was not loaded before evaluation
- Fixed infinite loop by adding max step constraint
- Ensured agent correctly followed commands after training

---

### Step 7: Visualization
Implemented reward tracking and plotting:
- Generated training reward curve
- Confirmed convergence behavior visually

---

## Key Challenges and Solutions

### Challenge 1: Infinite Loop During Evaluation
- **Issue:** Agent remained in same state due to empty Q-table
- **Solution:** Loaded trained Q-table before evaluation and added step limit

### Challenge 2: Policy Instability
- **Issue:** Agent failed to converge when trained on multiple commands
- **Solution:** Simplified training to a single command for controlled demonstration

### Challenge 3: Environment Compatibility
- **Issue:** Differences between Gym and Gymnasium APIs
- **Solution:** Updated reset() and step() handling to match Gymnasium return values

---

## Key Insight
A traditional RL agent learns a single task policy. In this project, the agent is conditioned on language input, meaning it must learn a mapping from text commands to behavior. This transforms the problem from static policy learning to dynamic, context-driven decision-making.

---

## Outcome
The agent successfully:
- Interpreted text-based commands
- Converted them into goal coordinates
- Navigated the GridWorld environment efficiently
- Reached the target in minimal steps

Example result:
> Command: "go to shelf B3"  
> Goal: (1, 2)  
> Steps: 3  
> Status: Success

---

## Reflection
This project demonstrates how NLP and RL can be integrated to create adaptive systems capable of interpreting human instructions and executing them in structured environments. The modular design also allows for future expansion, such as incorporating deep learning-based text embeddings or more complex environments.