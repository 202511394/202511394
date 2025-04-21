def display_multiplication_table(n):

    for i in range(n, n + 4):
        for j in range(1, 10):
            for k in range(i, min(i + 4, n + 9)):
                print(f"{k} x {j} = {k *  j}", end="\t")
            print()
        print()

display_multiplication_table(2)
