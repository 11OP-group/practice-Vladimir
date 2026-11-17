count = 0

for b in range(1,10):
    for k in range(1,20):
        for t in range(1,200):

            if 10*b + 5*k + 0.5*t == 100 and  (b + k + t) >= 1:
                count = count + 1
                print(f'вариант {count}: быков = {b}, коров = {k}, телят = {t}')
                break