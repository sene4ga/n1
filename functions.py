def prod_non_zero_diag(x):
    pr = 1
    i = 0
    j = 0
    ls = len(x[0])
    while i < len(x) and j < ls:
        if x[i][j] != 0: 
            pr *= x[i][j]
    return pr
    pass


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    return x == y
    pass

def max_after_zero(x):
    m = -1000000000
    for i in range(1,len(x)):
        if(x[i-1]==0 and x[i]>m):
            m = x[i]
    
    return m

    pass


def convert_image(img, coefs):
    h = len(img)
    w = len(img[0])
    res = list()
    for i in range(h):
        curr = list()
        for j in range(w):
            sum = 0
            for k in range(len(coefs)):
                sum += img[i][j][k] * coefs[k]
            curr.append(sum)
        res.append(curr)
    return res

    pass


def run_length_encoding(x):
    a = []
    b = []
    x.sort()
    i = 0
    while i < len(x):
        a.append(x[i])
        b.append(x.count(x[i]))
        i += x.count(x[i])

    return (a,b)
    pass


def pairwise_distance(x, y):
    res = list()
    for i in range(len(x)):
        curr = list()
        for j in range(len(y)):
            dist = 0
            for k in range(len(x[0])):
                d += (x[i][k] - y[j][k]) ** 2
            curr.append(math.sqrt(d))
        res.append(curr)
    return res

    pass
