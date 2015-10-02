import math

__author__ = 'Garance'
'''
This class represents a node in a peer to peer network.
A node is made of his number, and his routing table, or finger table.
'''

class Node:

    def __init__(self, n, N):
        self.n = n
        self.table = [None] * N

    def fill_table(self):
        for i in range(len(self.table)):
            self.table[i] = (self.n + math.pow(2, i)) % math.pow(2, len(self.table))
            # this is an intermediate result, we still have to find the real successors once we're in the network


    def node_nb(self):
        return self.n

    def finger(self):
        return self.table