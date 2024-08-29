from road import Road
from node import Node
from trafficGen import Traffic

class Enviroement:

    strada1 = Road(2, 5, [0, 0])
    strada2 = Road(1, 5, 0)

    node1 = Node([strada1, strada2], True)

    traffic = Traffic([strada1, strada2], 0.2)
    traffic.start()

    
