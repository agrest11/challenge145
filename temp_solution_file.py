def solution():
    # for one line test cases
    T = int(input())          # number of test cases
    for j in range(T):        # loop over all test cases
        # per test case
        done = []
        first_line = input().split()
        n, q = int(first_line[0]), int(first_line[1])         # test case first line input - n and q
        a = [int(element) for element in input().split()]           # second line input - array of size n
        for i in range(q):
            query = input().split()  # q lines of input
            if len(query) == 3:
                q_type, x, y = int(query[0]), int(query[1]), int(query[2])
                a[x-1], a[y-1] = a[y-1], a[x-1]
            elif len(query) == 2:
                q_type, x = int(query[0]), int(query[1])
                done.append(str(a[x-1]))
                out = " ".join(done)
        print(out)
