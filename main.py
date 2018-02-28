import fractal
from fractal_io import FractalIO
import genetic

from tqdm import tqdm

def main():
    imgsize = 200
    max_iter = 10
    inital_population = 10
    out_dir = "fractals"
    options = {
        "num_out":50,
        "num_new":10,
        "mutation_rate":0.1,
        "crossover_function":genetic.crossover_sample,
        "num_crossovers":30,
        "num_parents":5,
    }

    io = FractalIO(out_dir)
    current_gen = io.get_current_gen()

    if current_gen is 0:
        print("Starting to make the inital population")
        for _ in tqdm(range(inital_population)):
            coef, f = fractal.make_random_fractal(imgsize=imgsize)
            io.write_to_current_gen(coef, f, imgsize)
    else:
        print("On generation {}. Evolving generation {}".format(current_gen, current_gen-1))
        sucessful_coef = io.get_prev_gen_good()
        children = genetic.evolve(sucessful_coef, options)

        for child in tqdm(children):
            f = fractal.make_fractal(child, imgsize=imgsize, max_iter=max_iter)
            io.write_to_current_gen(child, f, imgsize)



if __name__ == '__main__':
    main()
