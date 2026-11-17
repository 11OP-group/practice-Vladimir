for n in range(1, 365 // 28 + 1):
    for k in range(1, 365 // 30 + 1):
        for m in range(1, 365 // 31 + 1):

            ostat = 365 - 28 * n - 30 * k

            if ostat >= 31 and ostat % 31 == 0:
                m = ostat // 31
                print(n, k, m)
                break