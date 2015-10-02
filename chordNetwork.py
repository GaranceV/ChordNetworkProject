import math

__author__ = 'Garance'
'''
This class represents a chord network.
A network is made of nodes.
You can join, quit,
'''

class ChordNetwork:

    def __init__(self):
        self.nodes = []

    def __str__(self):
        nodes_list = ""
        for index, node in enumerate(self.nodes):
            nodes_list += " N" + str(node.node_nb())
            nodes_list += ", "
        return nodes_list

    def join(self, newnode):
        for index, node in enumerate(self.nodes):
            if node.node_nb() >= newnode.node_nb():
                self.nodes.insert(index, newnode)
                return True
        self.nodes.append(newnode)
        return True

    def quit(self, node):
        self.nodes.remove(node)

    def fill_fingers(self):
        # for each node in the chord, we compute the fingers
        for index in range(len(self.nodes)):
            for i in range(6):
                # We must iterate over all the network again, to find the successor...
                # if the nb is > the biggest node, we must go back to 0
                if self.nodes[index].finger()[i] > self.nodes[len(self.nodes)-1].node_nb():
                    self.nodes[index].finger()[i] = 0
                for finalIndex in range(len(self.nodes)):
                        if self.nodes[index].finger()[i] <= self.nodes[finalIndex].node_nb():
                            self.nodes[index].finger()[i] = self.nodes[finalIndex].node_nb()
                            break
        return False

    def all_nodes(self):
        return self.nodes

    def successor(self, node):
        if self.nodes.index(node) < len(self.nodes)-1:
            return self.nodes[self.nodes.index(node)+1]
        return self.nodes[0]

    def get_a_node(self, nodeNb):
        for index in range(len(self.nodes)):
            if self.nodes[index].node_nb() == nodeNb:
                return self.nodes[index]
        return None