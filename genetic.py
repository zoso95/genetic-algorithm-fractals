import numpy as np
from scipy.stats import hmean
import fractal

def crossover_mean(list_of_coef):
    coefs = np.vstack(list_of_coef)
    return np.mean(coefs, axis=0)

def crossover_hmean(list_of_coef):
    coefs = np.vstack(list_of_coef)
    return hmean(coefs, axis=0)

def crossover_med(list_of_coef):
    coefs = np.vstack(list_of_coef)
    return np.median(coefs, axis=0)

def crossover_sample(list_of_coef):
    coefs = np.zeros(shape=list_of_coef[0].shape)
    for i in range(len(coefs)):
        ind = np.random.choice(np.arange(len(list_of_coef)), size=1)[0]
        coefs[i] = list_of_coef[ind][i]
    return coefs


def evolve(parents, options):

    output = []

    """
    Crossover winners
    """
    crossover_function = options.get("crossover_function", crossover_mean)
    num_crossovers = options.get("num_crossovers", len(parents)*(len(parents) - 1))
    num_parents = options.get("num_parents", 2)
    for _ in range(num_crossovers):
        ind = [i for i in np.random.choice(np.arange(len(parents)), replace=False, size=min(num_parents, len(parents)))]
        p = [parents[i] for i in ind]
        output.append(crossover_function(p))


    """Add some diversity"""
    for i in range(options.get("num_new", 5)):
        output.append(fractal.get_random_coef())

    """Mutate the parents"""
    mutation_rate = options.get("mutation_rate", 0.1)
    for p in parents:
        output.append(mutation(p, s=mutation_rate))

    # Randomly select output
    num_out = options.get("num_out", len(output))
    num_out = min(num_out, len(output))

    ind = np.arange(len(output))
    rand_ind = np.random.choice(ind, replace=False, size=num_out)

    final = list(np.array(output)[rand_ind])
    return final


def mutation(coef, s=0.1):
    # We don't want to turn on polynomials that weren't on initally
    c = coef.copy()
    ind = coef!=0
    c[ind] = c[ind] + np.random.normal(scale=s, size=c[ind].shape)
    return c
