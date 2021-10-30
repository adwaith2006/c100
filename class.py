class Car(object):
    def __init__ (self,model,color,company,speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
    
    def start(self):
        print("START")

    def stop(self):
        print("STOP")

    def accelerate(self):
        print("ACCELERATING")

Porsche= Car("911","red","porsche","300")
print(Porsche.model)
Porsche.accelerate()