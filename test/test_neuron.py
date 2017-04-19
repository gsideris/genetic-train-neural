import unittest
import os,sys,inspect
sys.path.append('..') 

from neural.neuron import Neuron

class NeuronTests(unittest.TestCase):

    def test_size(self):
        n = Neuron(10)
        self.failUnless(n.size == 10)

    def test_serialization(self):
        n = Neuron(10)

        original = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0]
        deserialized = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0]
        n.deserialize(deserialized)
        self.failUnless(len(deserialized) == 0)
        self.failUnless(n.serialize() == original)

    def test_sigmoid(self):
        n = Neuron(10)
        deserialized = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0]
        n.deserialize(deserialized)

        self.failUnless(str(n._sigmoid(0.5)) == str(0.622459331202))
        self.failUnless(str(n._sigmoid(0.0)) == str(0.5))
        self.failUnless(str(n._sigmoid(0.9)) == str(0.710949502625))
    
    def test_multiplication(self):
        n = Neuron(10)
        deserialized = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0]
        n.deserialize(deserialized)

        self.failUnless(n.multiply([1,2,3],[1,2,3]) == 14)
        self.failUnless(n.multiply([1,1,1],[1,1,1]) == 3)
    
    def test_forward(self):
        n = Neuron(3)
        n.deserialize([0.1,0.1,0.1])
        self.failUnless(str(n.forward([0.1,0.1,0.1])) == str(0.507499437551))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
