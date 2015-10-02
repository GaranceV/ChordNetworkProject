from node import Node
from chordNetwork import ChordNetwork

__author__ = 'Garance'
print("hello!! :)")

N = 6
#creation of every node for the exercise
n1 = Node(1, N)
n8 = Node(8, N)
n14 = Node(14, N)
n21 = Node(21, N)
n32 = Node(32, N)
n38 = Node(38, N)
n42 = Node(42, N)
n48 = Node(48, N)
n51 = Node(51, N)
n56 = Node(56, N)

#basic filling of the finger tables
n1.fill_table()
n8.fill_table()
n14.fill_table()
n21.fill_table()
n32.fill_table()
n38.fill_table()
n42.fill_table()
n48.fill_table()
n51.fill_table()
n56.fill_table()

#Creating the chord network
myNetwork = ChordNetwork()

#adding the nodes in the network
myNetwork.join(n1)
myNetwork.join(n8)
myNetwork.join(n14)
myNetwork.join(n21)
myNetwork.join(n32)
myNetwork.join(n38)
myNetwork.join(n42)
myNetwork.join(n48)
myNetwork.join(n51)
myNetwork.join(n56)

print(myNetwork)

#filling the finger tables now that we have the network topology
myNetwork.fill_fingers()

print(n1.finger())
print(n8.finger())
print(n14.finger())
print(n21.finger())
print(n32.finger())
print(n38.finger())
print(n42.finger())
print(n48.finger())
print(n51.finger())
print(n56.finger())


def closest_preceding_node(node, id):
    i = 5
    while i >= 0:
        currFinger = node.finger()[i]
        if currFinger < node.node_nb():
            currFinger += 64
        if node.node_nb() < currFinger < id:
            return myNetwork.get_a_node(node.finger()[i])
        i -= 1
    return node

def find_successor(node, id):
    if id <= node.node_nb():
        id += 64
    else:
        id %= 64
    hisSuccessor = myNetwork.successor(node).node_nb()
    if hisSuccessor < node.node_nb():
        hisSuccessor += 64
    if node.node_nb() < id <= hisSuccessor:
        return myNetwork.successor(node)
    else:
        newN = closest_preceding_node(node, id)
        return find_successor(newN, id)

print("Le successeur de " + str(n38.node_nb()) + " le plus proche pour arriver à 5 est " + str(
    find_successor(n38, 5).node_nb()))

print("Le successeur de " + str(n38.node_nb()) + " le plus proche pour arriver à 25 est " + str(
    find_successor(n38, 25).node_nb()))

print("Le successeur de " + str(n48.node_nb()) + " le plus proche pour arriver à 10 est " + str(
    find_successor(n48, 10).node_nb()))

print("Le successeur de " + str(n48.node_nb()) + " le plus proche pour arriver à 30 est " + str(
    find_successor(n48, 30).node_nb()))

print("Le successeur de " + str(n8.node_nb()) + " le plus proche pour arriver à 54 est " + str(
    find_successor(n8, 54).node_nb()))

print("Le successeur de " + str(n8.node_nb()) + " le plus proche pour arriver à 38 est " + str(
    find_successor(n8, 38).node_nb()))

print("Le successeur de " + str(n8.node_nb()) + " le plus proche pour arriver à 5 est " + str(
    find_successor(n8, 5).node_nb()))

print("Le successeur de " + str(n21.node_nb()) + " le plus proche pour arriver à 21 est " + str(
    find_successor(n21, 21).node_nb()))

print("Le successeur de " + str(n21.node_nb()) + " le plus proche pour arriver à 63 est " + str(
    find_successor(n21, 63).node_nb()))

print("Le successeur de " + str(n1.node_nb()) + " le plus proche pour arriver à 14 est " + str(
    find_successor(n1, 14).node_nb()))