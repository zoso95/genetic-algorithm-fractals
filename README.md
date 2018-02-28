# Intro
This is a simple library for using genetic algorithms to breed together cool fractals.

How it works is by running is by running main.py will run the next generation of fractal mixing.
1. If it hasn't run before, it will generate a random population
2. If it has run, the program will look at the latest generation, specifically in the folder "good"
and use that as a seed for the next generation.

To use this run main.py to seed generation 0, then
go into fractals/0 and move all the fractals you like into the good folder.
If you run this again, this will make fractals/1, and you can then move the ones you like into
fractals/1/good and repeat the process to your hearts contents.

# A few things to note
1. Render the fractals is expensive. So the GA part only renders small ones. If
You want good renders of the "good" fractals, the run make_fullsize_good.py, and that will rerender them.
2. The main.py has a lot of parameters in the options to control what the GA does. In summary they do

imgsize = image dimension size in pixels
max_iter = how many iterations to run newtons method for
inital_population = how many random ones to make in generation 0
out_dir = directory output for where you want you renders to go
options = {
    "num_out": max output for each generation,
    "num_new": number of randoms to generate and stick into each generation,
    "mutation_rate": error rate of coef in the parents
    "crossover_function": what crossover strategy to use,
    "num_crossovers": how many crossover children should we make,
    "num_parents": how many parents should be in each crossover,
}

# Things to be fun to mess around with
1. Different crossover strategies (can be found in genetic.py)
2. Different color maps (Any matplotlib one should work, Ive found these to be cool gist_yarg, prism, hot, jet, gist_gray, flag)
3. Different polynomial degrees, and different coef structures (right now the are normally distributed, but multipled by a
  binomial to turn off/on certain polynomial degrees)
