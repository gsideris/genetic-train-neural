## Genetic Training Neural Networks

This project provides a way to to use genetic algorithms to train a neural network.


### Genetic Package

example use:
<pre>
from genetic.genetic import Genetic
import random

# each individual of our population has a number of genes (float in this case)
# assume that the best fitness is the one that will have the maximum sum of all
# genes (ideally a list of [1.0,1.0 .... 1.0]
def fitness(individual):
        sum = 0.0
        for x in individual:
            sum += x
        return sum

# mutation function. This returns a random new gene.
def mutation():
    return random.random()

# create a genetic object of a pool of 100 individuals to evolve
# 200 genes per indiviual
# the fitness and mutation functions
genetic = Genetic(100,200,fitness,mutation)

# iterate 1000 generations with 0.4 mutation rate
genetic.iterate(1000,0.4)

# get the fittest score and the fittest indiviudual
fittest_score =  genetic.get_fittest_score()
fittest_individual = genetic.get_fittest_individual()

</pre>


### Neural Package

The neural package allows you to create a neural network, feed forward and serialize/deserialize. 
No other methods are implemented as genetic algorithms are used to train/test it.

example use:
<pre>
from neural.network import Network

# create a network of 5 inputs, hidden layers of 2 and 3 neurons and 2 as output
network = Network([5,2,3,2])

# out will have the 2 outputs after forwarding the inputs
inputs = [0.1,0.2,0.3,0.4,0.5]
out = network.forward(inputs);

# list has all the network data serialized
list = network.serialize()

# use list to deserialize a network
network.deserialize(list)
</pre>



### GeneticTrainNeural Package

This simply combines the two packages.

example use:

<pre>
from genetictrainnural import GeneticTrainingNeural
import random


# the individual is deserialized to a network
# that we need to test and evaluate
def fitness(network):
        test_output = network.forward(test_input)
        return how_good_is(test_output)
        
def mutation():
    return random.random()


individuals = 100
length = 200
iterations = 30000
mutation_rate = 0.4
neural_definition = [5,2,3,2]

gtn = GeneticTrainingNeural(individuals,neural_definition,fitness,mutation_rate)
# will print the fittest individual and its score
print gtn.train(iterations,mutation)

</pre>


### Example Game
In the game directory there is a simple game that we train a network.

The game takes place in a two dimensional world where a network has to move from position 
(1,1) to (9,9) without its health goes to 0. The network can move north,south,east and west. 
It can make only 100 maximum moves. At each move depending on the color of the tile health points
are reduced or added. A white tile is 0 added to the health, green is 1, red is -10, orange is -1
and black is a wall that the network can not pass through.

Depending on which stages trains and what parameters the network has, different actions are chosen.

A test network, trained passing test stages can be viewed in the live demo.

Just press run. If you have trained your network you can take the serialized/base64 version and place it
in the neural definition overriding the default

[https://gsideris.github.io/genetic-train-neural/game](https://gsideris.github.io/genetic-train-neural/game)


