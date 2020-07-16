def rec(prev, n):

    p = prev + 1

    count = 0

    if n > prev and prev != 0:

        count = 1  

    while(n - p > p ):

        count = count + rec(p, n - p)

        p = p + 1

    return count

print(rec(0, int(input())))
