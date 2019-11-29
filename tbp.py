"""
A three body problem simulation for testing the module
"""
import numpy as np
import matplotlib.pyplot as plt
from time import time
from mpl_toolkits.mplot3d import Axes3D

from world import World
from body import Body

w0 = World()

b0_pos = np.array([0,0,0])
b0_vel = np.array([0,0,0])

b1_pos = np.array([1,0,0])
b1_vel = np.array([0,1,0])

b2_pos = np.array([0,0,1])
b2_vel = np.array([[0,-1,0]])

w0.addBody(b0_pos, b0_vel, 1/w0.G, 0)
w0.addBody(b1_pos, b1_vel, 1/w0.G, 0)
w0.addBody(b2_pos, b2_vel, 1/w0.G, 0)

N = int(1e5)
dt = 1e-4

track = np.empty([len(w0.bodies),N,w0.dim])

print("Calculating orbits.")
t_start = time()

for i in range(N):
    w0 *= dt
    for j in range(len(w0.bodies)):
        track[j,i] = w0.bodies[j].pos

print(f"Time elapsed: {time() - t_start}")

print("Plotting orbits.")
t_start = time()

fig = plt.figure()
ax = plt.axes(projection="3d")

for i in range(len(w0.bodies)):
    ax.scatter3D(*np.transpose(track[i])[:,0])
    ax.plot3D(*np.transpose(track[i]), label=f"Body: {i}")

print(f"Time elapsed: {time() - t_start}")

plt.legend()
plt.show()
