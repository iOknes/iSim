# iSim: A basic Python physics simulation

## Structure:

### Object oriented apporach:

The basis of this program is an object oriented
approach to storing the simulated bodies.
To this end the simulaton implements a world object
to store all bodies in a simulation. These objects
have three basic properties:
* **G** - the gravitational constant *default: 6.67e-11*
* **K** - Coulomb's constnat *default: 8.99e9*
* **Cap** - The worlds body-capacity *default: 128*
