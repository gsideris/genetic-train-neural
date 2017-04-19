import unittest
import os,sys,inspect
sys.path.append('..') 

from neural.network import Network

class NetworkTests(unittest.TestCase):

    def test_size(self):
        network = Network([5,2,3,2])
        self.assertTrue(network.size() == 22)


    def test_serialize(self):
        network = Network([5,2,3,2])
        l = network.serialize()
        self.assertTrue(len(l) == 22)
        l2 = l[:]
        self.assertTrue(str(l) == str(l2))
        network.deserialize(l)
        self.assertTrue(len(l) == 0)
        l3 = network.serialize()
        self.assertTrue(str(l3) == str(l2))



def main():
    unittest.main()

if __name__ == '__main__':
    main()
