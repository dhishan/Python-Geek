def list_changer(list_1):
    list_1[0] = 5
    print(list_1)
    yield
    list_1 = range(1,5)
    yield
    print(list_1)
