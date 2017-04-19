import random
import math


# A neuron class
################

class Neuron(object):
    def __init__(self,size):
        self.size = size    # the number of weights
        self.randomize()    # put random values to weights
    
    # randomize the neuron's weights
    def randomize(self):
        self.weights = []
        for i in range(1,self.size+1):
            self.weights.append(random.random())
            
    # the basic sigmoid functions            
    def _sigmoid(self,value):
        return (1.0 / (1.0 + math.exp(-value)))
        
    # feed forward. multiply the inputs with the weights
    # and apply the sigmoid
    def forward(self,input_matrix):
        return self._sigmoid(self.multiply(self.weights,input_matrix))
        

    # multiplication of two matrices        
    def multiply(self,matrix1,matrix2):
        if len(matrix1) == len(matrix2):
            _sum = 0
            for i in range (len(matrix1)):
                _sum = _sum + matrix1[i] * matrix2[i]
        else:               
            message = "Matrices should have the same size %s != %s" % (len(matrix1), len(matrix2))
            raise ValueError(message)
        return _sum
        
    # serializes the weights as a list        
    def serialize(self):
        return self.weights
        
    # deserialize the weights from a list        
    def deserialize(self,list):
        self.weights = list[0:self.size]
        del list[0:self.size]
        
        

