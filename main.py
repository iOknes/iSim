import numpy as np

class object:
    def __init__(self, pos, vel, mass, charge):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.charge = charge
    
    @property
    def speed(self):
        return np.linalg.norm(self.vel)