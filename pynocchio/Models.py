import numpy as np

class Node:
    def __init__(self, inputs = []):
        self.inputs = inputs
        self.outputs = []

        for n in self.inputs:
            n.outpus.append(self)

        self.value = None

        self.gradients = {}

    def forward(self):

        raise NotImplemented

    def backward(self):

        raise NotImplemented

class PlaceHolder(Node):
    def __init__(self,name = None, istrainable = None):
        Node.__init__(self, name = name, istrainable = istrainable)

    def forward(self,value = None):
        if value is not None:
            self.value = value


class Linear(Node):
    def __init__(self,x = None,weight = None,bias =None, name = None, istrainable = False):
        Node.__init__(self,[x,weight,bias],name = name ,istrainable = istrainable)

    def forward(self):
        x,k,b = self[0],self[1],self[2]
        self.value = k.value * x.value + b.value

    def backward(self):
        x, k, b = self[0], self[1], self[2]
        for n in self.gradients:
            grad_cost = n.gradients[self]
            self.gradients[x] = k.value * grad_cost
            self.gradients[k] = x.value * grad_cost
            self.gradients[b] = 1 * grad_cost


