# Tyler Applin 59020616

import math
import random

random.seed(4)


class Particle:
    # Initalize new particle
    def __init__(self, dimension):
        self.dimension = dimension
        self.position = [random.uniform(-5.12, 5.12) for i in range(dimension)]
        self.velocity = [0 for j in range(dimension)]
        self.personal_best_position = self.position
        self.personal_best_fit = float("inf")

    # Calculates fitness of particle
    def calc_fitness(self):
        fit = 10 * self.dimension
        for i in range(len(self.position)):
            fit += (self.position[i] ** 2) - (10 * math.cos(2 * math.pi * self.position[i]))
        return fit

    # sets the velocity
    def set_velocity(self, velocity):
        self.velocity = velocity

    # Updates the position of particle
    def update_position(self):
        self.position = [self.position[i] + self.velocity[i] for i in range(self.dimension)]


class ParticleSwarm:
    # Initialize new particle swarm
    def __init__(self, dimension, num_particles, max_iter, w, c1, c2):
        self.swarm = [Particle(dimension) for i in range(num_particles)]
        self.max_iter = max_iter
        self.dimension = dimension
        self.neigh_best_fit = float("inf")
        self.neigh_best_position = None
        self.w = w
        self.c1 = c1
        self.c2 = c2

    # Updates the personal best for each particle in the swarm
    def update_p_best(self):

        for particle in self.swarm:
            particle_fitness = particle.calc_fitness()
            if particle_fitness < particle.personal_best_fit:
                if len(particle.position) == len(list(x for x in particle.position if -5.12 <= x <= 5.12)):
                    particle.personal_best_fit = particle_fitness
                    particle.personal_best_position = particle.position

    # sets the neighbourhood best for the swarm
    def set_neigh_best(self):
        for particle in self.swarm:
            if particle.personal_best_fit < self.neigh_best_fit:
                self.neigh_best_fit = particle.personal_best_fit
                self.neigh_best_position = particle.personal_best_position

    # Calculates the velocity update for each particle
    def calc_new_velocity(self):
        new_velocity = [0 for i in range(self.dimension)]
        for particle in self.swarm:
            x_max = 5.12
            x_min = -5.12
            v_max = (x_max - x_min) / 2
            for i in range(particle.dimension):
                v_i = (self.w * particle.velocity[i]) + \
                      (self.c1 * random.uniform(0, 1)) * (particle.personal_best_position[i] - particle.position[i]) + \
                      (self.c2 * random.uniform(0, 1)) * (self.neigh_best_position[i] - particle.position[i])
                if v_i < -1 * v_max:
                    new_velocity[i] = -1 * v_max
                elif v_i > v_max:
                    new_velocity[i] = v_max
                else:
                    new_velocity[i] = v_i

            particle.set_velocity(new_velocity)
            particle.update_position()


def fitness(solution):
    fit = 10 * len(solution)
    for i in range(len(solution)):
        fit += (solution[i] ** 2) - (10 * math.cos(2 * math.pi * solution[i]))
    return fit

if __name__ == '__main__':
    # User input
    num_parts = int(input("Enter the number number of particles: "))
    max_iterations = int(input("Enter the max number of iterations: "))
    w = float(input("Enter Inertia Component: "))
    c1 = float(input("Enter Cognitive Component: "))
    c2 = float(input("Enter Social Component: "))

    # initialize particles & velocity
    swarm = ParticleSwarm(30, num_parts, max_iterations, w, c1, c2)
    random_search = [random.uniform(-5.12, 5.12) for i in range(swarm.dimension)]
    random_search_best_solution = random_search

    count = 0

    while count < swarm.max_iter:
        swarm.update_p_best()
        swarm.set_neigh_best()
        swarm.calc_new_velocity()

        random_search = [random.uniform(-5.12, 5.12) for j in range(swarm.dimension)]

        if fitness(random_search) < fitness(random_search_best_solution):
            random_search_best_solution = random_search

        count += 1

    random_best = [random_search_best_solution, fitness(random_search_best_solution)]
    print("Random Best Position: " + str(random_best[0]))
    print("Random Best Fitness: " + str(random_best[1]))

    global_best = [swarm.neigh_best_position, swarm.neigh_best_fit]
    print("Global Best Position: " + str(global_best[0]))
    print("Global Best Fitness: " + str(global_best[1]))
