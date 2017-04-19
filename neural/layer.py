from neuron import Neuron

# The Layer class
#################

class Layer(object):
    def __init__(self,neuron_number,weight_number):
        self.neuron_number = neuron_number  # number of neurons
        self.weight_number = weight_number  # number of weights
        self.randomize()
        

    # randomize all neurons of the layer        
    def randomize(self):
        self.neurons = []
        for i in range(1,self.neuron_number+1):
            self.neurons.append(Neuron(self.weight_number))
            
    # forward the inputs to all the neurons of the layer
    def forward(self,input_matrix):
        outputs = []
        for n in self.neurons:
            outputs.append(n.forward(input_matrix))
            
        return outputs
        
    # serialize all the neuron data to a list
    def serialize(self):
        _list = []
        # serialize all neurons
        for n in self.neurons:
            _list.append(n.serialize())
        # return a flattened list            
        return [item for sublist in _list for item in sublist]          
        
    # deserialize from a list all the neuron data        
    def deserialize(self,list):
        for n in self.neurons:
            n.deserialize(list)
            
            
            

