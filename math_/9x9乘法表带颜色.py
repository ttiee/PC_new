for i in range(1, 10):
    for j in range(1, i+1):
        print('\033[4;3{3}m{1}x{0}={2}\033[0m'.format(i, j, i*j, i-1), end='\t')
    print()