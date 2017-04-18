from genetic.genetic import Genetic
from neural.network import Network
import random

class GeneticTrainingNeural(object):
    def __init__(self,pool,neural_def,fitness_func,mutation_rate):
        self.pool = pool
        self.neural_def = neural_def
        network = Network(neural_def)
        self.length = network.size()
        self.mutation_rate = mutation_rate
        self.fitness_func = fitness_func


    def train(self,iterations,mutation_func):
        genetic = Genetic(self.pool,self.length,self.evaluate,mutation_func)
        genetic.iterate(iterations,self.mutation_rate)
        return genetic.get_fittest_individual(),genetic.get_fittest_score()


    def genes_to_network(self,individual):
        network = Network(self.neural_def)
        network.deserialize(individual[:])
        return network

    def network_to_genes(self,network):
        return network.serialize()


    def evaluate(self,individual):
        network = self.genes_to_network(individual)
        return self.fitness_func(network)

