
class FlyingBird:

    def __init__(self, speed):
        self.fl_speed = speed
    
    def fly(self):
        print(f"I am flying at speed {self.fl_speed}")


class RunningBird:

    def __init__(self, speed):
        self.rn_speed = speed
        
    def run(self):
        print(f"I am running at speed {self.rn_speed}")

class Duck(FlyingBird, RunningBird): 

    def __init__(self, rn_speed, fl_speed):
        FlyingBird.__init__(self, fl_speed)
        RunningBird.__init__(self, rn_speed)

d = Duck(10, 15)
d.fly()
d.run()