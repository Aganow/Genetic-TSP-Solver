import random

class GeneticTSPSolver:
	def __init__(self, cities, population_size=100, elite_size=10, mutation_rate=0.01):
		self.cities = cities
		self.population_size = population_size
		self.elite_size = elite_size
		self.mutation_rate = mutation_rate

	def distance(self, city1, city2):
		# Calculate the Euclidean distance between two cities
		x1, y1 = city1
		x2, y2 = city2
		return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

	def initial_population(self):
		# Generate an initial population of routes
		population = []
		for _ in range(self.population_size):
			population.append(random.sample(self.cities, len(self.cities)))
		return population

	def route_distance(self, route):
		# Calculate the total distance of a route
		total_distance = 0
		for i in range(len(route)):
			city1 = route[i]
			city2 = route[(i + 1) % len(route)]
			total_distance += self.distance(city1, city2)
		return total_distance

	def breed_population(self, population):
		# Perform crossover and mutation to create a new population
		children = []
		elite = population[:self.elite_size]

		# Crossover
		for _ in range(self.population_size - self.elite_size):
			parent1, parent2 = random.sample(population, 2)
			child = self.order_crossover(parent1, parent2)
			children.append(child)

		# Mutation
		for child in children:
			self.swap_mutation(child)

		return elite + children

	def order_crossover(self, parent1, parent2):
		# Perform order crossover between two parents
		start_index = random.randint(0, len(parent1) - 2)
		end_index = random.randint(start_index + 1, len(parent1) - 1)
		child = parent1[start_index:end_index]

		for city in parent2:
			if city not in child:
				child.append(city)

		return child

	def swap_mutation(self, route):
		# Perform swap mutation on a route
		for i in range(len(route)):
			if random.random() < self.mutation_rate:
				j = random.randint(0, len(route) - 1)
				route[i], route[j] = route[j], route[i]

	def solve(self, generations=100):
		# Solve the TSP using a genetic algorithm
		population = self.initial_population()

		for _ in range(generations):
			population = self.breed_population(population)

		best_route = min(population, key=self.route_distance)
		return best_route, self.route_distance(best_route)
