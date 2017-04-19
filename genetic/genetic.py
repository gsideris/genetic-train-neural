from random import randint, random
import math
import datetime


# The Genetic class
###################

class Genetic(object):
    # constructor:
    #   population size : The number of individuals that will evolve
    #   individual size : Each individual is a list of floats (genes).
    #                     This represents the number of floats.
    #   fitness_class   : a function that accepts an individual and
    #                     returns a fitness score
    #   mutation_class  : a function that will provide a random value
    #                     to set to an individual's gene(float)


    def __init__(self,population_size,individual_size,fitness_class,mutation_class):
        self.population_size = population_size
        self.individual_size = individual_size
        self.fitness_class = fitness_class
        self.mutation_class = mutation_class
        # create the initial population
        self.create_population()
        # evaluate and sort before we start evolving
        self.evaluate_and_sort()
            
    # helper function that creates a random individual            
    def create_list(self,size):
        _list = []
        for i in range(1,size+1):       
            _list.append(random()) 
        return _list

    # creates the population. A list of individuals to evolve
    def create_population(self):
        self.population = []
        for i in range(1,self.population_size+1):       
            self.population.append(self.create_list(self.individual_size))

    
    
    # evolves a generation. 
    #   position is the position to split and combine two individuals
    #   mutation rate is the percentage(from 0.0 to 1.0) that mutation 
    #                 will take place
    def evolve(self,position,mutation_rate):
            half = self.population_size / 2
            quarter = self.population_size / 4
    
            for selection in range (quarter):
           
              # selection. select the top quarter of idividuals
              # to crossover
              parent1 = self.population[selection]
              parent2 = self.population[half - selection]
    
              # crossover and produce two children
              # AAAAA and BBBBB will give AABBB and BBAAA
              child1 = []
              child2 = []
              for i in range(position):
                    child1.append(parent1[i])
                    child2.append(parent2[i])
              
              for i in range(position,self.individual_size):              
                    child2.append(parent1[i])
                    child1.append(parent2[i])

    
              # mutate if necessary
              if random() < mutation_rate:
                 pos = randint(0,self.individual_size -1)
                 child1[pos] = self.mutation_class()
                 child2[pos] = self.mutation_class()
              
              # set the offspring to the population
              self.population[half+selection] = child1
              self.population[self.population_size - 1 - selection] = child2
    
    # iterate. Apply evolution for a number of generatiions            
    def iterate(self,generation_number,mutation_rate):            
        # we start with the lowest score
        score = float('-inf')

        # iterate 
        for n in range(1,generation_number+1):            
            # sort and find best and wors
            self.evaluate_and_sort()
            fittest_score = self.get_fittest_score()
            unfittest_score = self.get_unfittest_score()
            if score < fittest_score:
                score = fittest_score
                print "Generation %s : (%s) (%s) %s" % (n,fittest_score,unfittest_score,datetime.datetime.now())
            elif n % 100 == 0:                
                print "Generation %s : (%s) (%s) %s" % (n,fittest_score,unfittest_score,datetime.datetime.now())
            pos = randint(1,len(self.population[0])-1)
            # evolve
            self.evolve(pos,mutation_rate) # TODO set position to initialize
               
            
    # helper to get the fittest        
    def get_fittest_individual(self):
        return self.population[0]
    
    # helper to get the fittest's score
    def get_fittest_score(self):
        return self.fitness_class(self.population[0])
            
    # helper to find the unfittest        
    def get_unfittest_score(self):
        return self.fitness_class(self.population[-1])
    
    # helper to sort the population of idividuals
    def evaluate_and_sort(self):
        self.population.sort(key=lambda x:self.fitness_class(x),reverse=True)
    
    
    

