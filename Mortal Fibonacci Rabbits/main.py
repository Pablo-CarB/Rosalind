
# T(n)=T(n-1)+T(n-2)*2-t(n-m)
def mortal_fib(n,m):
    T_a = 1
    T_b = 1
    T_c = 2

    for i in range(4,n+1):
        # switching T_c and T_b
        T_b = T_b + T_c
        T_c = T_b - T_c
        T_b = T_b - T_c

        # switching T_b and T_a
        T_