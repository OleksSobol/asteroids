# Asteroids

A simple Asteroids game implemented in Go.

## Features

- Classic Asteroids gameplay
- Player-controlled spaceship
- Asteroids with random movement and splitting
- Shooting mechanics
- Collision detection
- Score tracking

## Getting Started

### Prerequisites

- Go 1.18 or newer

### Installation

Clone the repository:

```bash
git clone https://github.com/olekssobol/asteroids.git
cd asteroids
```

### Running the Game

```bash
go run .
```

## Project Structure

- `main.go`: Entry point, game loop, window management
- `game.go`: Core game logic, state management
- `player.go`: Player ship controls and rendering
- `asteroid.go`: Asteroid behavior and rendering
- `bullet.go`: Bullet logic and collision
- `utils.go`: Utility functions (math, collision, etc.)

## Controls

- **Arrow keys / WASD**: Move and rotate ship
- **Space**: Shoot
- **Esc / Q**: Quit

## License

MIT License

---

*Enjoy blasting asteroids!*