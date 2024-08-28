from road import Road
from node import Node

strada1 = Road(2, 5, [0, 0])
strada2 = Road(1, 5, 0)

node1 = Node([strada1, strada2], True)

for stoplight in node1.stoplight:
    print(stoplight.state)
