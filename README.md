# Maze Solver

This project is a **Maze Solver** implemented in Python using the Tkinter
library for graphical interface. The program generates and solves mazes using
the **Depth First Search (DFS)** algorithm.

## Features

- **Maze Generation**: Generate a visual maze dynamically.
- **Maze Solver**: Solve the generated maze using the Depth First Search
  algorithm.
- **GUI**: Interactive graphical user interface built with Tkinter.
- **Unit Tests**: Includes unit tests for validating functionality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jackheywood/maze_solver.git
   cd maze_solver
   ```

2. Ensure you have **Python 3** and **tkinter** installed on your system.

3For Unix-based systems, ensure `main.sh` and `test.sh` have execution
permissions:

   ```bash
   chmod +x main.sh
   chmod +x test.sh
   ```

## Usage

### Running the Maze Solver

To launch the program, execute the following command:

```bash
./main.sh
```

This will open the GUI which will generate and solve a random maze.

### Running Unit Tests

To ensure everything is working as expected, run the test script:

```bash
./test.sh
```

___

This project was build following the
[Build a Maze Solver](https://www.boot.dev/courses/build-maze-solver-python)
course on [Boot.dev](https://www.boot.dev).
