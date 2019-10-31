from body import Body

class RigidBody(Body):
    def __init__(self, pos, mass, charge):
        self.pos = pos
        self.vel = 0
        self.mass = mass
        self.charge = charge

    @staticmethod
    def fromBody(body):
        return RigidBody(body.pos, body.mass, body.charge)
