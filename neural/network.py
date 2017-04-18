from layer import Layer

class Network(object):
    # accepts a list of number of neurons for each layer
    # eg [5,2,3,2] will create 3 layers
    # layer 1 2x5 (5 inputs to 2 neurons)
    # layer 2 3x2 (2 inputs to 3 neurons)
    # layer 3 3x2 (3 inputs to 2 neurons/outputs)

    def __init__(self,structure):
        self.layers = []
        for i in range(len(structure) - 1):
            self.layers.append(Layer(structure[i+1], structure[i]))
            
    def forward(self,input_matrix):
        output = input_matrix
        for layer in self.layers:
            output = layer.forward(output)
        return output
        
    def serialize(self):
        _list = []
        for l in self.layers:
            _list.append(l.serialize())
        #print "Serializing netgwork with : %s" % len([item for sublist in _list for item in sublist])          
        return [item for sublist in _list for item in sublist]  
        
    def deserialize(self,list):
        for l in self.layers:
            l.deserialize(list)

    def size(self):
        return len(self.serialize())


