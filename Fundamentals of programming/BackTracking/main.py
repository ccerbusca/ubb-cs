
def is_set(x, m):
    if len(set(x)) != len(x):
        return False
    i = 0
    while i < len(x) - 1:
        if abs(x[i] - x[i + 1]) < m:
            return False
        i += 1
    return True

def iterative(x, n, m):
    x = [0]
    found = False
    while len(x) > 0:
        chosen = False
        while not chosen and x[-1] < n:
            x[-1] += 1
            chosen = is_set(x, m)
        if chosen:
            if len(x) == n:
                print(x)
                found = True
            else:
                x.append(0)
        else:
            x = x[:-1]
    return found

def recursive(x, n, m, found):
    if len(x) == n:
        print(x)
        found[0] = True
    if len(x) > n:
        return
    x.append(0)
    for i in range(1, n + 1):
        x[-1] = i
        if is_set(x, m):
            recursive(x[:], n, m, found)

if not iterative([], 5, 2):
    print("No solutions for the specified m and n")

print()

found = [False]
recursive([], 5, 2, found)
if not found[0]:
    print("No solutions for the specified m and n")
