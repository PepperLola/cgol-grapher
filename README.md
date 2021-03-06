# Conway's Game of Life Grapher

This program creates a graph with the number of cells in a CGOL (Conway's Game of Life) game on the y-axis and the generation on the x-axis. Useful if you want to observe patterns in the population.

If you're just looking for software that lets you play around with CGOL, I highly recommend [Golly](http://golly.sourceforge.net "Golly").

## IMPORTANT

Make sure you have these installed:
* [Python 3](https://python.org "Python") (of course)
* [Matplotlib](https://matplotlib.org "Matplotlib")

You can install Matplotlib by running `pip install matplotlib` in the command prompt (or Terminal if you're using Mac).

## Instructions

First, you will have to run the program. To do this, you must navigate to the folder you put the program in and type `python cgol_grapher.py`. This will run the program.

## Command Line Arguments

Without any arguments, the program will run with a 40x40 cell grid size and wait 0.05s in between generations. If you want to change these, you can use `--size` or `--wait`. For example, `python cgol_grapher --size 128 --wait 1` would run the program with a grid size of 128x128 and it would wait 1s in between.

Once you run the program, you will be asked to input which cells you want to be alive, like this:

![Instructions](https://github.com/PepperLola/cgol-grapher/blob/master/docsbutnotactuallydocs/assets/example_r-pentomino.png?raw=true "Instructions")

This is an [R-Pentomino](http://www.conwaylife.com/wiki/R-pentomino "R-Pentomino").

X represents the X-value, Y the Y-value (like on a Euclidean plane, except the origin is the top-left).

You can also choose to generate a random board. Do this by entering `random/probability of alive cell`, like this:

![Random Board](https://github.com/PepperLola/cgol-grapher/blob/master/docsbutnotactuallydocs/assets/random_board.png?raw=true "Random Board")

I chose 0.5, meaning there would be a 50/50 chance of getting an alive cell vs a dead cell for each tile.

Next, you are asked how many generations you would like it to simulate.

![Generations](https://github.com/PepperLola/cgol-grapher/blob/master/docsbutnotactuallydocs/assets/generations_input.png?raw=true "Generations Input")

I chose 1000, but it doesn't matter what you chose. Just keep in mind that you probably want to choose a number greater than the number of generations it will take for your pattern to stabilize.

The program will proceed to simulate the game, as shown here:

![Simulation](https://github.com/PepperLola/cgol-grapher/blob/master/docsbutnotactuallydocs/assets/simulating_game.png?raw=true "Simulation")

This is just your ordinary CGOL simulation, except a little worse :)

Now, the graph.
Once the program is finished with the number of generations you inputted, it will create a graph, like this one:

![Graph](https://github.com/PepperLola/cgol-grapher/blob/master/docsbutnotactuallydocs/assets/graph.png?raw=true "Graph")

That's it! You're all done.

pls don't judge