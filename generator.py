def fibbonacci(cnt):
    a, b = -1, 1
    while cnt:
        c = a + b
        yield c
        a, b = b, c
        cnt -= 1
