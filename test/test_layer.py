import unittest
import os,sys,inspect
sys.path.append('..') 

from neural.layer import Layer

class LayerTests(unittest.TestCase):

    def test_size(self):
        l = Layer(3,4)
        self.assertTrue(len(l.serialize()) == 12)

    def test_serialization(self):
        l = Layer(3,4)
        data = l.serialize()
        data2 = data[:]
        self.assertTrue(str(data) == str(data2))
        
        l.deserialize(data2)
        self.assertTrue(len(data2) == 0)
        self.assertTrue(str(l.serialize()) == str(data))

    def test_serialization_fail(self):
        l = Layer(3,4)
        data = l.serialize()
        data2 = data[:]
        data2 = data2[::-1]
        l.deserialize(data2)
        self.assertTrue(len(data2) == 0)
        self.assertFalse(str(l.serialize()) == str(data))



def main():
    unittest.main()

if __name__ == '__main__':
    main()
