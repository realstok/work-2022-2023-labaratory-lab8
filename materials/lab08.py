import math


def add_noneg_ints(u, v, b):
    n = len(u)
    j = n
    k = 0
    w = list()

    for i in range(1, n+1):
        w.append(
            (int(u[n-i]) + int(v[n-i]) + k) % b
        )

        k = (int(u[n-i]) + int(v[n-i]) + k)//b
        j = j - 1
    w.reverse()
    return w


def sub_noneg_ints(u, v, b):
    n = len(u)
    j = n
    k = 0
    w = list()

    for i in range(1, n+1):
        w.append(
            (int(u[n-i]) - int(v[n-i]) + k) % b
        )

        k = (int(u[n-i]) - int(v[n-i]) + k)//b
        j = j - 1
    w.reverse()
    return w


def mul_noneg_ints_col(u, v, b):
    n = len(u)
    m = len(v)

    w = list()
    for i in range(m+n):
        w.append(0)
    j = m

    def step6():
        nonlocal j
        nonlocal w
        j = j - 1
        if j > 0:
            step2()
        if j == 0:
            print(w)

    def step2():
        nonlocal v
        nonlocal w
        nonlocal j
        if j == m:
            j = j-1
        if int(v[j]) == 0:
            w[j] = 0
            step6()

    def step4():
        nonlocal k
        nonlocal t
        nonlocal i
        if i == n:
            i = i - 1
        t = int(u[i]) * int(v[j]) + w[i + j] + k
        w[i + j] = t % b
        k = t / b

    def step5():
        nonlocal i
        nonlocal w
        nonlocal j
        nonlocal k
        i = i - 1
        if i > 0:
            step4()
        else:
            w[j] = k

    step2()
    i = n
    k = 0
    t = 1
    step4()
    step5()
    step6()
    print(w)


def quick_col(u, v, b):
    n = len(u)
    m = len(v)
    b = 10
    w1 = list()
    for i in range(m+n+2):
        w1.append(0)
    t1 = 0
    for s1 in range(0, m+n):
        for i1 in range(0, s1+1):
            if n-i1 > n or m-s1+i1 > m or n-i1 < 0 or m-s1+i1 < 0 or m-s1+i1-1 < 0:
                continue
            t1 = t1 + (int(u[n-i1-1]) * int(v[m-s1+i1-1]))
        w1[m+n-s1-1] = t1 % b
        t1 = math.floor(t1/b)
    return w1


def div_multi_bit_ints(u, v, b):
    n = len(u) - 1
    t = len(v) - 1
    q = list()
    for j in range(n-t):
        q.append(0)
    r = list()
    for j in range(t):
        r.append(0)

    while int(u) >= int(v)*(b**(n-t)):
        q[n-t] = q[n-t] + 1
        u = int(u) - int(v)*(b**(n-t))
    u = str(u)
    for i in range(n, t+1, -1):
        v = str(v)
        u = str(u)
        if int(u[i]) > int(v[t]):
            q[i-t-1] = b - 1
        else:
            q[i-t-1] = math.floor((int(u[i])*b + int(u[i-1]))/int(v[t]))

        while (int(q[i-t-1])*(int(v[t])*b + int(v[t-1])) > int(u[i])*(b**2) + int(u[i-1])*b + int(u[i-2])):
            q[i-t-1] = q[i-t-1] - 1
        u = (int(u) - q[i-t-1]*b**(i-t-1)*int(v))
        if u < 0:
            u = int(u) + int(v) * (b**(i-t-1))
            q[i-t-1] = q[i-t-1] - 1
    r = u
    return q, r


print(add_noneg_ints("12345", "56789", 10))
print(sub_noneg_ints("56789", "12345", 10))
mul_noneg_ints_col("123456", "7890", 10)
print(quick_col("12345", "6789", 10))
print(div_multi_bit_ints("12346789", "56789", 10))
