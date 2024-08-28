class Road:
    
    def __init__(self, laneNumber=2, roadLenght=1, car=[0, 0]):

        self.roadLength = roadLenght #la lunghezza equivale al metro in proporzione 1:5
        self.laneNumber = laneNumber #numero di corsie

        if laneNumber == 2:
            self.carNumber = [car[0], car[1]]
            self.trafficDensity = [(self.carNumber[0]/roadLenght), (self.carNumber[1]/roadLenght)]
            #densità del traffico presente in ogni unità di lunghezza

        elif laneNumber == 1: 
            self.trafficDensity = 0.0
            self.carNumber = car
        
