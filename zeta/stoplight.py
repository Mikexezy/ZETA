class StopLight:

    def turn(self, newState):
        if newState == -1:
            self.state = "rosso"
        elif newState == 0:
            self.state = "giallo"
        elif newState == 1:
            self.state = "verde"
        else:
            print("semaforo guasto")
    
    def __init__(self, state):
        self.turn(state)

    