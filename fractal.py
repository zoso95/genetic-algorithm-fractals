import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def get_random_coef(size=10):
    return np.random.normal(size=size)*np.random.binomial(n=1, p=0.3, size=size)

def make_random_fractal(imgsize=1000, max_iter=200, verbose=False):
    coef = get_random_coef()
    return coef, make_fractal(coef, imgsize=imgsize, max_iter=max_iter, verbose=verbose)

"""
This is a macro that will print out strings you need for f(z) and df(z)
if you want to change the power of the polynomial. You will also want to change the size variable in
get_random_coef
"""
def print_f_df(power):
    f = ""
    df = ""
    for i in range(power):
        f += "coef[{}]".format(i)+"*z"*i + "+"
        if i>0:
            df += "{}*coef[{}]".format(i, i)+"*z"*(i-1) + "+"
    print(f[:-1])
    print(df[:-1])


def make_fractal(coef, imgsize=1000, max_iter=200, verbose=False):
    if verbose:
        print("Creating fractal for ", coef)
    def f(z):
        return coef[0]+coef[1]*z+coef[2]*z*z+coef[3]*z*z*z+coef[4]*z*z*z*z+coef[5]*z*z*z*z*z+coef[6]*z*z*z*z*z*z+coef[7]*z*z*z*z*z*z*z+coef[8]*z*z*z*z*z*z*z*z+coef[9]*z*z*z*z*z*z*z*z*z
    def df(z):
        return 1*coef[1]+2*coef[2]*z+3*coef[3]*z*z+4*coef[4]*z*z*z+5*coef[5]*z*z*z*z+6*coef[6]*z*z*z*z*z+7*coef[7]*z*z*z*z*z*z+8*coef[8]*z*z*z*z*z*z*z+9*coef[9]*z*z*z*z*z*z*z*z

    y, x = np.ogrid[1: -1: imgsize*2j, -1: 1: imgsize*2j]
    z = x +y*1j

    img = np.zeros(z.shape)
    it = range(max_iter)
    if verbose:
        it = tqdm(range(max_iter))
    for i in it:
        z = z - f(z)/df(z)
        ind = np.logical_and(np.abs(f(z)) < 1e-4, img==0)
        img[ind] = i

    return img

def save(img, outfile, cmap="gist_yarg", imgsize=1000):
    fig = plt.figure(figsize=(imgsize/100.0, imgsize/100.0), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis('off')
    ax.imshow(img, cmap=cmap)
    fig.savefig(outfile)
    plt.close(fig)
