
def double_all(nums):
    return [x * 2 for x in nums]

def square_dict(nums):
    return {x: x * x for x in nums}

def pairwise_sum(xs, ys):
    return [a + b for a, b in zip(xs, ys)]

def consecutive_pairs(xs):
    return list(zip(xs, xs[1:]))

def square_generator(n):
    return (i * i for i in range(1, n + 1))

