from body import Body

class RigidBody(Body):
    def __init__(self, pos, mass, charge):
        self._pos = pos
        self._vel = 0
        self._mass = mass
        self._charge = charge

    @staticmethod
    def fromBody(body):
        return RigidBody(body.pos, body.mass, body.charge)
