from neuron import Neuron

class Layer(object):
    def __init__(self,neuron_number,weight_number):
        self.neuron_number = neuron_number
        self.weight_number = weight_number
        self.randomize()
        
    def randomize(self):
        self.neurons = []
        for i in range(1,self.neuron_number+1):
            self.neurons.append(Neuron(self.weight_number))
            
    def forward(self,input_matrix):
        outputs = []
        for n in self.neurons:
            outputs.append(n.forward(input_matrix))
            
        return outputs
        
    def serialize(self):
        _list = []
        for n in self.neurons:
            _list.append(n.serialize())
        #print "Serializing layer with : %s" % len([item for sublist in _list for item in sublist])          
        return [item for sublist in _list for item in sublist]          
        
    def deserialize(self,list):
        for n in self.neurons:
            n.deserialize(list)
            
            
            

