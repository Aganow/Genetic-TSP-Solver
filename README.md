# GeneticTSPSolver: Genetic Algorithm for Traveling Salesman Problem

The `GeneticTSPSolver` module is a powerful tool for solving the Traveling Salesman Problem (TSP) using a genetic algorithm approach. The TSP is a classic optimization problem where the objective is to find the shortest possible route that visits a set of cities and returns to the starting city.

This module provides an implementation of a genetic algorithm specifically tailored for solving the TSP. It offers a flexible and efficient solution by combining techniques such as population generation, crossover, and mutation. 

## Key Features

- **Population Generation:** The module generates an initial population of routes using a random sampling technique.
- **Fitness Evaluation:** The algorithm evaluates the fitness of each route by calculating the total distance traveled, considering the Euclidean distance between cities.
- **Crossover:** Order crossover technique is employed to create new offspring routes by combining two parent routes.
- **Mutation:** Swap mutation is applied to introduce variation in the population, increasing the chances of finding better solutions.
- **Elitism:** The algorithm preserves a certain number of top-performing routes (elite) in each generation, ensuring that the best solutions are not lost.

## Usage

To utilize the `GeneticTSPSolver` module, follow these steps:

1. Install the module by downloading the Python file from the GitHub repository.
2. Import the module into your Python script or interactive environment.
3. Create a list of cities, representing their coordinates (e.g., `[(0, 0), (1, 5), (2, 3), ...]`).
4. Instantiate the `GeneticTSPSolver` class, passing the cities list and optionally setting other parameters such as population size, elite size, and mutation rate.
5. Invoke the `solve()` method to start the optimization process. You can specify the number of generations to run (default is 100).
6. Retrieve the best route and its corresponding distance from the returned values.
7. Utilize the obtained solution for further analysis, visualization, or decision-making processes.

Here's an example of the usage:

```python
from GeneticTSPSolver import GeneticTSPSolver

cities = [(0, 0), (1, 5), (2, 3), (7, 2), (4, 6)]
solver = GeneticTSPSolver(cities)
best_route, distance = solver.solve()

print("Best Route:", best_route)
print("Distance:", distance)
```

The module provides an effective means of solving the TSP using a genetic algorithm, allowing users to find optimized routes for their specific sets of cities.
