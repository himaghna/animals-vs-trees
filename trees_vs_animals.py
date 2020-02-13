"""
@uthor: Himaghna, 17th August 2019
Description: Track the population of trees (feed on solar energy)
and animals which feed on plants
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Animals:
    def __init__(self):
        self.population = np.array([])

    def set_population(self, population_trajectory):
        """Expose the population trajectory of the ecosystem
        population_trajectory: numpy ndarray(float) population
        trajectory of the system
        """
        self.population = np.concatenate(
            (self.population, population_trajectory))

class Plants:
    def __init__(self):
        self.population = np.array([])

    def set_population(self, population_trajectory):
        """Expose the population trajectory of the ecosystem
        population_trajectory: numpy ndarray(float) population
        trajectory of the system
        """
        self.population = np.concatenate(
            (self.population, population_trajectory))

def main():
    #parameters
    simulation_time = 10
    solar_energy = 10  # total energy to feed plants
    animal_eating_rate = 0.7  # P(animal eating plant)
    animal_death_rate = 0.1 # fraction of animals that die from natural causes
    plant_death_rate = 0.4
    # initialize populations and instances
    init_plant_pop = 50
    init_animal_pop = 1
    plant_ecosystem = Plants()
    animal_ecosystem = Animals()

    def population_model(plant_animal_pop, t):
        """
        Set up the population model
        plant_pop: plant population
        animal_pop: animal population
        return: [d plant_pop/dt, d animal_pop/ dt]
        """
        plant_pop = plant_animal_pop[0]
        animal_pop = plant_animal_pop[1]
        d_plant_pop = solar_energy/plant_pop - animal_eating_rate * animal_pop - plant_death_rate * plant_pop
        d_animal_pop = animal_eating_rate * plant_pop/animal_pop - animal_death_rate * animal_pop
        return [d_plant_pop, d_animal_pop]
    t = np.linspace(0, simulation_time, simulation_time * 10000)
    initial_plant_animal_pop = [init_plant_pop, init_animal_pop]
    plant_animal_pop = odeint(population_model, initial_plant_animal_pop, t)
    plant_ecosystem.set_population(plant_animal_pop[:,0])
    animal_ecosystem.set_population(plant_animal_pop[:,1])

    # plot results
    plt.figure()
    plt.plot(t, plant_ecosystem.population, label='Plants', c='red')
    plt.plot(t, animal_ecosystem.population, label='Animals', c='blue')
    plt.xlabel('Simulation Time')
    plt.ylabel('Population')
    plt.title(f'Initial Plants {init_plant_pop}, Initial Animals {init_animal_pop}')
    plt.legend(loc=0)
    plt.show()

if __name__ == "__main__":
    main()
