import numpy as np
from body import Body
from rigidbody import RigidBody

class World:
    def __init__(self, G=6.67e-11, K=8.99e9, cap=128):
        self.G = G
        self.K = K
        self.bodies = np.empty(cap, dtype=Body)

    def joinBody(self, body):
        self.bodies[len(self.bodies[self.bodies != None])] = body

    def addBody(self, pos, vel, mass, charge, rigid=False):
        body = RigidBody(pos, mass, charge) if rigid else Body(pos, vel, mass, charge)
        self.joinBody(body)

    def __mul__(self, dt):
        a = 0
        self.bodies = Body.move(self.bodies, a, dt)
        return self

    def __imul__(self, dt):
        return self * dt

    def getAcc(self, gravity=True, elmag=False):
        acc = np.empty(len(self.bodies))
        for body in self.bodies[self.bodies != None]:
            
            pass