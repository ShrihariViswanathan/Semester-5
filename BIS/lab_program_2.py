f = lambda x: x**2

n = 2

x = [4, 2]
v = [0, 0]
fit = [0 for _ in range(n)]

w = 1
iterations = 2

c1 = 1
c2 = 1

r1 = 0.213
r2 = 0.876

p_best = x.copy()
g_best = min(p_best, key=f)


def vel_update(vi, idx):
    xi = x[idx]
    p_besti = p_best[idx]

    new_v = (w * vi
             + c1 * r1 * (p_besti - xi)
             + c2 * r2 * (g_best - xi))

    return new_v


def pos_update(xi, new_v):
    return xi + new_v


def fitness():
    for i in range(n):
        fit[i] = f(x[i])
    return fit


for t in range(iterations):

    # Step 1: Calculate fitness
    fitness()

    # Step 2: Update velocity and position
    for i in range(n):

        new_v = vel_update(v[i], i)
        new_x = pos_update(x[i], new_v)

        v[i] = new_v
        x[i] = new_x

        # Step 3: Update Pbest
        if f(new_x) < f(p_best[i]):
            p_best[i] = new_x

    # Step 4: Update Gbest
    g_best = min(p_best, key=f)

    print("Iteration:", t + 1)
    print("Positions:", x)
    print("Velocities:", v)
    print("Pbest:", p_best)
    print("Gbest:", g_best)
    print("Fitness:", [f(i) for i in x])
    print("--------------------")


    




