from GeneticTSPSolver import GeneticTSPSolver

cities = [(0, 0), (1, 5), (2, 3), (7, 2), (4, 6)]
solver = GeneticTSPSolver(cities)
best_route, distance = solver.solve()

print("Best Route:", best_route)
print("Distance:", distance)
