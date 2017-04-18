from genetic import Genetic
import random

def fitness(individual):
        sum = 0.0
        for x in individual:
            sum += x
        return sum
def mutation():
    return random.random()

pool = 100
length = 200
iterations = 30000
mutation_rate = 0.4
genetic = Genetic(pool,length,fitness,mutation)
before = genetic.get_fittest_score()
genetic.iterate(iterations,mutation_rate)
print "----------"
after =  genetic.get_fittest_score()
print before,after
