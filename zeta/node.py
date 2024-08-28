from stoplight import StopLight

class Node:
    def __init__(self, connectedRoads=[], checked=True):
        self.connectedRoads = connectedRoads
        self.stoplight = []
        
        if checked == True: #configura tutti i semafori necessari
            for i in range(len(self.connectedRoads)):
                self.stoplight.append(StopLight(0))
        else: 
            self.stoplight = False