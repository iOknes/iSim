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

    def __str__(self):
        return f"pos: {self.pos}, vel: {self.vel}, mass: {self.mass}"

    @property
    def speed(self):
        return np.linalg.norm(self.vel)

    @staticmethod
    def getPos(bodyArray):
        n = len(bodyArray)
        posArray = np.empty(n, dtype=np.array)
        for i in range(n):
            posArray[i] = bodyArray[i].pos
        return posArray

    @staticmethod
    def getVel(bodyArray):
        n = len(bodyArray)
        velArray = np.empty(n, dtype=np.array)
        for i in range(n):
            velArray[i] = bodyArray[i].vel
        return velArray

    @staticmethod
    def move(bod, a, dt):
        try:
            va = body.getVel(bod)
            vh = va + a * dt**2 / 2
            pa = body.getPos(bod) + vh * dt
            va = vh + a * dt**2 / 2
            for i in range(len(bod)):
                bod[i].pos = pa[i]
                bod[i].vel = va[i]
        except TypeError:
            vh = bod.vel * a * dt**2 / 2
            bod.pos += vh * dt
            bod.vel = vh + a * dt**2 / 2
        return bod

class rigidBody(body):
    def __init__(self, pos, mass, charge):
        self.pos = pos
        self.vel = 0
        self.mass = mass
        self.charge = charge
    
    @staticmethod
    def fromBody(bod):
        return rigidBody(bod.pos, bod.mass, bod.charge)

class world:
    def __init__(self, G=6.67e-11, K=8.99e9, cap=128):
        self.G = G
        self.K = K
        self.bodies = np.empty(cap, dtype=body)
    
    def addBody(self, pos, vel, mass, charge, rigid=False):
        try:
            if rigidBody:
                self.bodies[len(self.bodies) - len(self.bodies[self.bodies == None])] = rigidBody(pos, mass, charge)
            else:
                self.bodies[len(self.bodies) - len(self.bodies[self.bodies == None])] = body(pos, vel, mass, charge)
        except IndexError:
            raise Exception("World capacity exceeded!")

    def joinBody(self, body):
        self.bodies[len(self.bodies) - len(self.bodies[self.bodies == None])] = body

    def __mul__(self, dt):
        a = 0
        self.bodies = body.move(self.bodies, a, dt)
        return self
    
    def __imul__(self, dt):
        return self * dt
