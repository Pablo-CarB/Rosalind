def fib_bunnies(n,k):

    F_a = 1
    F_b = 1

    for i in range(3,n+1):
        F_a = F_b + F_a
        F_b = F_a - F_b
        F_a = F_a - F_b

        F_b = F_b*k + F_a

    return F_b


print(fib_bunnies(28,2))
