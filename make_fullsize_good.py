import fractal
import os
from fractal_io import FractalIO

from tqdm import tqdm

def main():
    io = FractalIO("fractals", make_new=False)
    out_dir = "full_res"

    imgsize = 1500
    max_iter = 10

    for vg in io.valid_gen:
        print("Handling generation ", vg)

        directory = os.path.join(*[out_dir, str(vg)])
        if not os.path.exists(directory):
            os.makedirs(directory)

        for coef in tqdm(io.get_prev_gen_good(str(vg))):

            s = [str(c) for c in list(coef)]
            serialized_file = "[{}].png".format(" ".join(s))
            outfile = os.path.join(*[directory, serialized_file])

            if os.path.isfile(outfile):
                continue

            f = fractal.make_fractal(coef, imgsize=imgsize, max_iter=max_iter)
            fractal.save(f, outfile, imgsize=imgsize)




if __name__ == '__main__':
    main()
