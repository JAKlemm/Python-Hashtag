class Hashtag:

    n = int(input("Enter number of rows: "))

    for i in range(1, n + 1):
        print("#", end = "")
        for j in range(0, i):
            print(" ", end = "")
        print("#")
        