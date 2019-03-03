# Conway's Game of Life Grapher

This program creates a graph with the number of cells in a CGOL (Conway's Game of Life) game on the y-axis and the generation on the x-axis. Useful if you want to observe patterns in the population.

If you're just looking for software that lets you play around with CGOL, I highly recommend [Golly](https://golly.sourceforge.net "Golly").

## IMPORTANT

Make sure you have these installed:
* [Python 3](https://python.org "Python") (of course)
* [Matplotlib](https://matplotlib.org "Matplotlib")

You can install Matplotlib by running `pip install matplotlib` in the command prompt (or Terminal if you're using Mac).

## Instructions

First, you will be asked to input which cells you want to be alive.

Here's an example:
![Instructions](https://github.com/PepperLola/cgol-grapher/blob/master/images/example_r-pentomino.png?raw=true "Instructions")

This is an [R-Pentomino](http://www.conwaylife.com/wiki/R-pentomino "R-Pentomino").

X represents the X-value (like on a Euclidean plane, except the origin is the top-right), Y the Y-value and S the state you want that cell to be in. The state is pretty much useless, because everything starts out dead, but eh.

Next, you are asked how many generations you would like it to simulate.

![Generations](https://github.com/PepperLola/cgol-grapher/blob/master/images/generations_input.png?raw=true "Generations Input")

I chose 1000, but it doesn't matter what you chose, but keep in mind that you probably want to choose a number greater than the number of generations it will take for your pattern to stabilize.

The program will proceed to simulate the game, as shown here:

![Simulation](https://github.com/PepperLola/cgol-grapher/blob/master/images/simulating_game.png?raw=true "Simulation")

This is just your ordinary CGOL simulation.

Now, the graph.
Once the program is finished iterating through the number of generations you inputted, it will create a graph, like this one:

![Graph](https://github.com/PepperLola/cgol-grapher/blob/master/images/graph.png?raw=true "Graph")

That's it! You're all done.