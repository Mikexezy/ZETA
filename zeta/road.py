class Road:
    
    def __init__(self, laneNumber=2, roadLength=1, car=[0, 0], nodeN=0):
        self.nodeN = nodeN
        self.roadLength = roadLength #la lunghezza equivale al metro in proporzione 1:5
        self.laneNumber = laneNumber #numero di corsie

        if laneNumber == 2:
            self.carNumber = [car[0], car[1]]
            self.trafficDensity = [(self.carNumber[0]/roadLength), (self.carNumber[1]/roadLength)]
            #densità del traffico presente in ogni unità di lunghezza

        elif laneNumber == 1: 
            self.trafficDensity = 0.0
            self.carNumber = car
        
