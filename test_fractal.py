import fractal

def main():
    imgsize = 100
    _, f = fractal.make_random_fractal(imgsize=imgsize, verbose=True)
    fractal.save(f, "test.png", imgsize=imgsize)

if __name__ == '__main__':
    main()
