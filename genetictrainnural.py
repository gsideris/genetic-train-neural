from genetic.genetic import Genetic
from neural.network import Network
import random

# GenetricTrainingNeural class
#   helps to user the genetic and neural packages
#################################################

class GeneticTrainingNeural(object):
    # constructior:
    #   pool         : the number of population
    #   neural_def   : the definition (list of size of layers) of the network
    #   fitness_func : the fitness function
    #   mutation_rate: the mutation rate (0.0,1.0)
    def __init__(self,pool,neural_def,fitness_func,mutation_rate):
        self.pool = pool
        self.neural_def = neural_def
        network = Network(neural_def)
        self.length = network.size()
        self.mutation_rate = mutation_rate
        self.fitness_func = fitness_func


    # creates the genetic and evolves the network
    def train(self,iterations,mutation_func):
        genetic = Genetic(self.pool,self.length,self.evaluate,mutation_func)
        genetic.iterate(iterations,self.mutation_rate)
        return genetic.get_fittest_individual(),genetic.get_fittest_score()


    # mapping individual to network using the network's deserialization
    def genes_to_network(self,individual):
        network = Network(self.neural_def)
        network.deserialize(individual[:])
        return network

    # mapping a network to an induvudual using the network's serialization
    def network_to_genes(self,network):
        return network.serialize()


    # evaluate: this deserializes the network gets its fitness
    # the fitness function accepts a network.
    def evaluate(self,individual):
        network = self.genes_to_network(individual)
        return self.fitness_func(network)

