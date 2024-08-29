import random
import time
from threading import Thread

class Traffic(Thread):
        
    def __init__(self, spawnRoad=[{}], spawnDelay=1):
        Thread.__init__(self)
        self.spawnRoad = spawnRoad
        self.spawnDelay = spawnDelay

    def run(self):
        while True:
            time.sleep(self.spawnDelay)  # delay in secondi

            available_roads = [road for road in self.spawnRoad 
                               if (isinstance(road.carNumber, list) and road.carNumber[1] < road.roadLength) or
                               (not isinstance(road.carNumber, list) and road.carNumber < road.roadLength)]
            
            if not available_roads:
                print("Tutte le strade sono piene. Nessuna macchina può essere aggiunta.")
                continue

            randomRoad = random.choice(available_roads)

            if isinstance(randomRoad.carNumber, list):
                remaining_space = randomRoad.roadLength - randomRoad.carNumber[1]
                if remaining_space > 0:
                    newCar = random.randint(1, remaining_space)
                    randomRoad.carNumber = [randomRoad.carNumber[0], randomRoad.carNumber[1] + newCar] 
                    print("Aggiunte sulla strada 1", randomRoad.carNumber)
                else:
                    print(f"Strada 1 è piena con {randomRoad.carNumber[1]} macchine.")
            else:
                remaining_space = randomRoad.roadLength - randomRoad.carNumber
                if remaining_space > 0:
                    newCar = random.randint(1, remaining_space)
                    randomRoad.carNumber += newCar
                    print("Aggiunte sulla strada 2", randomRoad.carNumber)
                else:
                    print(f"Strada 2 è piena con {randomRoad.carNumber} macchine.")