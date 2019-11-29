"""
A simulation of planetary orbits, for testing the module.
"""
import numpy as np
import matplotlib.pyplot as plt
from time import time
from mpl_toolkits.mplot3d import Axes3D

from world import World
from body import Body

w0 = World()

mercury_pos = np.array([2.482457691136895E+10, 4.010991965362851E+10, 8.635523682687823E+08])
mercury_vel = np.array([-5.056616436201271E+04, 2.850041505208587E+04, 6.966862106913164E+03])
mercury_mass = 3.285e23

venus_pos = np.array([3.043847272216039E+10, -1.032026891160324E+11, -3.215531269702129E+09])
venus_vel = np.array([3.332530175747475E+04 , 9.837914285608647E+03, -1.788529521785596E+03])
venus_mass = 4.867e24

earth_pos = np.array([9.511001264805460E+10, 1.134711975365665E+11, -5.141145183004439E+07])
earth_vel = np.array([-2.330578193434303E+04, 1.901622076647900E+04, -1.627765065719267])
earth_mass = 5.972e24

mars_pos = np.array([-2.405974222936806E+11, -4.591598323825889E+10, 4.906815267791769E+09])
mars_vel = np.array([5.547062227496759E+03, -2.170821906824929E+04, -5.908971621054260E+02])
mars_mass = 6.39e23

w0.addBody(np.zeros(3), np.zeros(3), 1.99e30, 0)
w0.addBody(mercury_pos, mercury_vel, mercury_mass, 0)
w0.addBody(venus_pos, venus_vel, venus_mass, 0)
w0.addBody(earth_pos, earth_vel, earth_mass, 0)
w0.addBody(mars_pos, mars_vel, mars_mass, 0)

N = int(60 * 24 * 365)
dt = 60

print(len(w0.bodies))

track = np.empty([len(w0.bodies),N,w0.dim])

for i in w0.bodies:
    print(i)

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
    ax.scatter3D(*np.transpose(track[i])[:,0], marker="*")
    ax.scatter3D(*np.transpose(track[i])[:,-1])
    ax.plot3D(*np.transpose(track[i]), label=f"Body: {i}")

print(f"Time elapsed: {time() - t_start}")

plt.legend()
plt.show()
