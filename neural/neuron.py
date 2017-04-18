import random
import math

class Neuron(object):
    def __init__(self,size):
        self.size = size
        self.randomize()
        
    def randomize(self):
        self.weights = []
        for i in range(1,self.size+1):
            self.weights.append(random.random())
            
    def _sigmoid(self,value):
        return (1.0 / (1.0 + math.exp(-value)))
        
    def forward(self,input_matrix):
        return self._sigmoid(self.multiply(self.weights,input_matrix))
        
    def multiply(self,matrix1,matrix2):
        if len(matrix1) == len(matrix2):
            _sum = 0
            for i in range (len(matrix1)):
                _sum = _sum + matrix1[i] * matrix2[i]
        else:               
            message = "Matrices should have the same size %s != %s" % (len(matrix1), len(matrix2))
            raise ValueError(message)
        return _sum
        
    def serialize(self):
        #print "Serializing neuron with : %s" % len(self.weights)
        return self.weights
        
    def deserialize(self,list):
        self.weights = list[0:self.size]
        del list[0:self.size]
        
        

