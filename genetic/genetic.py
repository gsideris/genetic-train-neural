from random import randint, random
import math
import datetime


class Genetic(object):
    def __init__(self,population_size,individual_size,fitness_class,mutation_class):
        self.population_size = population_size
        self.individual_size = individual_size
        self.fitness_class = fitness_class
        self.mutation_class = mutation_class
        self.create_population()
        self.evaluate_and_sort()
            
    def create_list(self,size):
        _list = []
        for i in range(1,size+1):       
            _list.append(random()) 
        return _list

    def create_population(self):
        self.population = []
        for i in range(1,self.population_size+1):       
            self.population.append(self.create_list(self.individual_size))

    
    
    
    def evolve(self,position,mutation_rate):
            half = self.population_size / 2
            quarter = self.population_size / 4
    
            for selection in range (quarter):
           
              # selection
              parent1 = self.population[selection]
              parent2 = self.population[half - selection]
    
              # crossover
              child1 = []
              child2 = []
              for i in range(position):
                    child1.append(parent1[i])
                    child2.append(parent2[i])
              
              for i in range(position,self.individual_size):              
                    child2.append(parent1[i])
                    child1.append(parent2[i])

    
              # mutate
              if random() < mutation_rate:
                 pos = randint(0,self.individual_size -1)
                 child1[pos] = self.mutation_class()
                 child2[pos] = self.mutation_class()
              
              # set the offspring to the population
              self.population[half+selection] = child1
              self.population[self.population_size - 1 - selection] = child2
    
            
    def iterate(self,generation_number,mutation_rate):            
        score = float('-inf')
        for n in range(1,generation_number+1):            
            self.evaluate_and_sort()
            fittest_score = self.get_fittest_score()
            unfittest_score = self.get_unfittest_score()
            if score < fittest_score:
                score = fittest_score
                print "Generation %s : (%s) (%s) %s" % (n,fittest_score,unfittest_score,datetime.datetime.now())
            elif n % 100 == 0:                
                print "Generation %s : (%s) (%s) %s" % (n,fittest_score,unfittest_score,datetime.datetime.now())
            pos = randint(1,len(self.population[0])-1)
            #self.evolve(5,mutation_rate) # TODO set position to initialize
            self.evolve(pos,mutation_rate) # TODO set position to initialize
               
            
        
    def get_fittest_individual(self):
        return self.population[0]
    

    def get_fittest_score(self):
        return self.fitness_class(self.population[0])
            
        
    def get_unfittest_score(self):
        return self.fitness_class(self.population[-1])
    
    def evaluate_and_sort(self):
        self.population.sort(key=lambda x:self.fitness_class(x),reverse=True)
    
    
    

