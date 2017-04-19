import unittest
import os,sys,inspect
sys.path.append('..') 
import random

from genetic.genetic import Genetic

def fitness(individual):
        sum = 0.0
        for x in individual:
            sum += x
        return sum

def mutation():
    return random.random()

class GeneticTests(unittest.TestCase):
    def test_run(self):
        genetic = Genetic(50,100,fitness,mutation)
        before = genetic.get_fittest_score()
        genetic.iterate(1000,0.4)
        after =  genetic.get_fittest_score()

        self.assertTrue(before < after)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
