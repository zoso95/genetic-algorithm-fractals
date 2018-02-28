import numpy as np
import os
import fractal

class FractalIO:

    def __init__(self, directory, make_new=True):
        self.directory = directory

        if not os.path.exists(directory):
            os.makedirs(directory)

        dirs = []
        for x in os.walk(directory):
            if x[0] is self.directory:
                dirs = x[1]

        print(dirs)

        if len(dirs) > 0:
            self.valid_gen = [int(d) for d in dirs]
            last_gen = max(self.valid_gen)
            self.current_gen = last_gen + 1
        else:
            self.valid_gen = []
            self.current_gen = 0

        if make_new:
            self.out_dir = os.path.join(self.directory, str(self.current_gen))
            good_path = os.path.join(self.out_dir, "good")
            bad_path = os.path.join(self.out_dir, "bad")

            for d in [self.out_dir, good_path, bad_path]:
                os.makedirs(d)

    def get_current_gen(self):
        return self.current_gen

    def write_to_current_gen(self, coef, f, imgsize):
        s = [str(c) for c in list(coef)]
        serialized_file = "[{}].png".format(" ".join(s))
        outfile = os.path.join(self.out_dir, serialized_file)
        fractal.save(f, outfile, imgsize=imgsize)

    def get_prev_gen_good(self, generation=None):
        if generation:
            old_out = os.path.join(self.directory, generation)
        else:
            old_out = os.path.join(self.directory, str(self.current_gen - 1))
        good = os.path.join(old_out, "good")
        print("Reading in ", good)

        files = [f for f in os.listdir(good) if os.path.isfile(os.path.join(good, f))]
        coefs = []

        for f in files:
            if "DS" in f:
                continue
            arr = np.fromstring(f[1:-5], dtype=float, sep=' ')
            coefs.append(arr)
        print("Found", len(coefs), "results")
        return coefs
