def read_file():
    r = [0, 0, 0, 0, 0, 0]
    file = open('rollstest.txt', 'r')
    file = file.readlines()
    for lis in file:
        lis = lis.split('\t')
        print(lis)
        c = input()
        for l in lis:
            pass
