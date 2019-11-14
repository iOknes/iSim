from world import World
from body import Body
from rigidbody import RigidBody
import numpy as np
import matplotlib.pyplot as plt

w0 = World(G=1)
w0.addBody(np.array([0,0]), np.array([0,0]), 1, 0)
w0.addBody(np.array([1,0]), np.array([0,1]), 0, 0)
#w0.addBody(np.array([0,0]), np.array([0,0,]), 1, 0)
#w0.addBody(np.array([1,1,0,0]), np.array([0,0,0,0]), 1, 0)
print("t0")
for i in w0.bodies:
    print(i)

plt.scatter(*w0.bodies[0].pos)

N = int(6.5e5)
trace = np.empty([N,2])

for i in range(N):
    w0 *= 1e-5
    trace[i] = w0.bodies[1].pos

plt.scatter(*np.transpose(trace))
#plt.axis([-1.5,1.5,-1.5,1.5])
plt.axes().set_aspect("equal")
plt.savefig()
