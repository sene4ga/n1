import numpy as np


def prod_non_zero_diag(x):
    n = x.diagonal()
    m = n[n!=0]
    return np.prod(m)
    pass


def are_multisets_equal_v(x, y):

    return np.sort(x) == np.sort(y)



def max_after_zero(x):
    return np.max(x[1:][(x==0)[:-1]])

    pass


def convert_image(img, coefs):
    return np.sum(img * coefs, axis=-1)

    pass


def run_length_encoding(x):
    y = np.hstack((np.ones(1), x[:- 1]))
    first_positions = x != y
    first_positions[0] = True
    indexes_1 = np.arange(np.size(x))[first_positions]
    indexes_2 = np.hstack((indexes_1[1:], np.array([np.size(x)])))
    return x[first_positions], indexes_2 - indexes_1

    pass


def pairwise_distance(x, y):
    return np.sqrt(np.sum((X[:, np.newaxis] - Y) ** 2, axis=-1))

    pass
