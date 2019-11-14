import numpy as np
from body import Body
from rigidbody import RigidBody

class World:
    def __init__(self, G=6.67e-11, K=8.99e9):
        self.G = G
        self.K = K
        self.bodies = np.empty(0, dtype=Body)

    def joinBody(self, body):
        self.bodies = np.concatenate((self.bodies, body), axis=None)

    def addBody(self, pos, vel, mass, charge, rigid=False):
        body = RigidBody(pos, mass, charge) if rigid else Body(pos, vel, mass, charge)
        self.joinBody(body)

    @property
    def dim(self):
        try:
            return len(self.bodies[0].pos)
        except TypeError:
            print("No bodies in world!")

    def getAcc(self, gravity=True, elmag=False):
        n = len(self.bodies)
        acc = np.ones([n, self.dim])
        for i in range(n):
            #print(f"Body {i}:")
            bodies = self.bodies[self.bodies != self.bodies[i]]
            dist = Body.getPos(bodies)
            dist -= self.bodies[i].pos
            #print(f"Dist: {dist}")
            distnorm = np.linalg.norm((dist), axis=1)
            mass = Body.getMass(bodies)
            #print(f"Mass: {mass}")
            #print(f"Dist: {dist}")
            #print(f"Distnorm: {distnorm}")
            accarr = self.G * mass * dist
            dnq = distnorm**3
            #print(f"Dnq: {dnq}")
            accarr /= dnq
            #print(f"Accarr: {accarr}")
            #print(f"Accarr_T: {np.transpose(accarr)}")
            accel = np.sum(np.transpose(accarr), 1)
            #print(f"Accel: {accel}")
            acc[i] = accel
        return acc

    def __mul__(self, dt):
        a = self.getAcc()
        self.bodies = Body.move(self.bodies, a, dt)
        return self

    def __imul__(self, dt):
        return self * dt
