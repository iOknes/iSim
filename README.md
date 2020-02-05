# pySim: A basic Python physics simulation

## Structure:

### The goals:

The goal of this Python package is to create a flexible, yet
fast, framework for creating simulations of physical phenomena.
It is meant to produce code that is fast, but not so fast that
human readability and flexibility is compromised. Fast writing
and modifying of code takes center stage, allowing for projects
to be completed in a reasonable time, while remaining 
understandable to the user of the module.

### Object oriented apporach:

The basis of this program is an object oriented
approach to storing the simulated bodies.
To this end the simulaton implements a *world* object
to store all bodies in a simulation. These objects
have three basic properties:
* **G** - the gravitational constant *default: 6.67e-11*
* **K** - Coulomb's constnat *default: 8.99e9*
* **Cap** - The worlds body-capacity *default: 128*
These can all be changed upon creation of a new world object.

The other major object in the structure is the *body* object.
This object is each representations of a point mass with a 
charge, given in kilograms and coulombs respectivly, as well
as a position and a velocity given in *meter* and *meters per*
*second* respectivly.
