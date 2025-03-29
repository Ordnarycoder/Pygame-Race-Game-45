# Race Game with Obstacles and Buffs

A simple race game built using Python and Pygame. In this game, the player controls a car that must avoid obstacles while collecting buffs. Obstacles and buffs are generated at random positions and move downward on the screen. Colliding with an obstacle ends the game, while collecting a buff applies a positive effect (e.g., reducing the car's speed).

## Features

- **Player Control:** Use the left and right arrow keys to move the car.
- **Obstacles:** Green rectangles that spawn at regular intervals and move downward. Colliding with an obstacle results in a game over.
- **Buffs:** Blue rectangles that spawn less frequently. Collecting a buff reduces the car's speed.
- **Dynamic Difficulty:** The speed of both the car and obstacles increases as the game progresses.
- **Basic Collision Detection:** Simple collision logic to detect interactions between the car, obstacles, and buffs.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) (Install via pip: `pip install pygame`)

## How to Run

1. **Clone the repository or download the source code:**
   ```bash
   git clone https://github.com/Ordnarycoder/Pygame-Race-Game-45
   cd race-game
