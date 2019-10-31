import numpy as np

class Body:
    def __init__(self, pos, vel, mass, charge):
        self._pos = pos
        self._vel = vel
        self._mass = mass
        self._charge = charge

    def __eq__(self, other):
        return np.all(self.pos == other.pos)

    def __ne__(self, other):
        return np.any(self.pos != other.pos)

    def __str__(self):
        return f"pos: {self.pos}, vel: {self.vel}, mass: {self.mass}"

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def vel(self):
        return self._vel

    @vel.setter
    def vel(self, vel):
        self._vel = vel

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        self.__mass = mass

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, charge):
        self._charge = charge

    @property
    def speed(self):
        return np.linalg.norm(self.vel)

    @staticmethod
    def getPos(bodyArray):
        posArray = bodyArray.pos
        """
        n = len(bodyArray)
        posArray = np.empty(n, dtype=np.array)
        for i in range(n):
            posArray[i] = bodyArray[i].pos
        """
        return posArray

    @staticmethod
    def getVel(bodyArray):
        velArray = bodyArray.vel
        """
        n = len(bodyArray)
        velArray = np.empty(n, dtype=np.array)
        for i in range(n):
            velArray[i] = bodyArray[i].vel
        """
        return velArray

    @staticmethod
    def move(body, a, dt):
        try:
            va = Body.getVel(body)
            vh = va + a * dt**2 / 2
            pa = Body.getPos(body) + vh * dt
            va = vh + a * dt**2 / 2
            for i in range(len(body)):
                body[i].pos = pa[i]
                body[i].vel = va[i]
        except TypeError:
            vh = body.vel * a * dt**2 / 2
            body.pos += vh * dt
            body.vel = vh + a * dt**2 / 2
        return body
