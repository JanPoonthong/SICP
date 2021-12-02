# Recursive solution
def fact(n):
    if n == 0:
        return  1
    else:
        return n * fact(n-1)

print(fact(4))

# Iterative
def fact_i(n):
    def fact_iter(acc, n):
        if n == 0:
            return acc
        else:
            return fact_iter(n*acc, n-1)
    return fact_iter(1, n)

print(fact_i(4))
