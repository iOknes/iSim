import numpy as np

class body:
    def __init__(self, pos, vel, mass, charge):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.charge = charge
    
    def __eq__(self, bod):
        return np.all(self.pos == bod.pos)
    
    def __ne__(self, bod):
        return np.any(self.pos != bod.pos)

    @staticmethod
    def move(self, dt, a):
        return self

    @property
    def speed(self):
        return np.linalg.norm(self.vel)

class world:
    def __init__(self, G=6.67e-11, K=8.99e9, cap=128):
        self.G = G
        self.K = K
        self.bodies = np.empty(cap, dtype=body)
    
    def addBody(self, pos, vel, mass, charge):
        try:
            self.bodies[len(self.bodies) - len(self.bodies[self.bodies == None])] = body(pos, vel, mass, charge)
        except IndexError:
            raise Exception("World capacity exceeded!")

    def __mlt__(self, dt):
        a = 0
        self.bodies = self.bodies.move(dt, a)
        return self
