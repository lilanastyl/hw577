import itertools
# Завдання 1 (9 варіант)
# Побудова таблиці істинності для f(x, y, z) = ((x | y) AND z)(x OR y)
def task_1():
    print("task 1: Таблиця істинності")
    print("f(x, y, z) = ((x | y) ∧ z) → (x ∨ y)")
    print("x | y | z | (x|y) | (x|y)&z | x∨y | f(x,y,z)")
    print("-" * 43)

    f_vector = []
    for x, y, z in itertools.product([0, 1], repeat=3):
        sh = int(not (x and y))
        az = int(sh and z)
        oxy = int(x or y)
        fv = int(not az or oxy)

        f_vector.append(str(fv))
        print(f"{x} | {y} | {z} |   {sh}   |    {az}    |  {oxy}  |    {fv}")

    print("\nВектор значень вийшов такий f(x,y,z):", "".join(f_vector))

# Завдання 2 (9 варіант)
# Суперпозиція функцій h(x, y) = f5(f4(x, y, x), y, x)

def task_2():

    print("task2: Суперпозиція функцій")
    print("h(x, y) = f5(f4(x, y, x), y, x)")

    f4_v = [0, 1, 1, 1, 1, 0, 1, 0]
    f5_v = [1, 1, 0, 0, 0, 1, 1, 1]

    def ef4(u, v, w):
        idx = u * 4 + v * 2 + w
        return f4_v[idx]

    def ef5(u, v, w):
        idx = u * 4 + v * 2 + w
        return f5_v[idx]

    print("x | y | f4(x,y,x) | h(x,y) = f5(f4(x,y,x), y, x)")
    print("-" * 48)

    h_vector = []
    for x, y in itertools.product([0, 1], repeat=2):
        inner = ef4(x, y, x)
        h_val = ef5(inner, y, x)
        h_vector.append(str(h_val))
        print(f"{x} | {y} | {inner} | {h_val}")

    print("\nВектор значень h(x,y):", "".join(h_vector))


# Завдання 3 (9 варіант)
# Пошук істотних та фіктивних змінних для f(x, y, z) = (0000 1010)

def task_3():

    print("task 3 Істотні та фіктивні змінні")
    print("f(x, y, z) = (0000 1010)")


    f_vector = [0, 0, 0, 0, 1, 0, 1, 0]

    def eff(x, y, z):
        return f_vector[x * 4 + y * 2 + z]

    var_names = ['x', 'y', 'z']
    evv = []
    dv = []

    for i, var_name in enumerate(var_names):
        is_essential = False
        for x, y, z in itertools.product([0, 1], repeat=3):
            t0 = [x, y, z]
            t1 = [x, y, z]
            t0[i] = 0
            t1[i] = 1

            if eff(*t0) != eff(*t1):
                is_essential = True
                break

        if is_essential:
            evv.append(var_name)
        else:
            dv.append(var_name)

    print(f"Суттєві (істотні) змінні: {evv}")
    print(f"Фіктивні змінні:          {dv}")
    print("\nФормула через істотні змінні: f(x, z) = x AND (NOT z)")


# Завдання 4 (9 варіант)
# Аналіз відношення rho: -x^2 + x + 10 <= -y^2 + y + 10

def task_4():

    print("ЗАВДАННЯ 4: Властивості відношення")


    X = [-7, -6.2, -5, -4.3, -0.25, 0, 0.5, 15, 510]

    def g(t):
        return -t ** 2 + t + 10

    def rho(x, y):
        return g(x) <= g(y)

    is_reflexive = all(rho(x, x) for x in X)
    is_transitive = all(
        rho(x, z)
        for x in X for y in X for z in X
        if rho(x, y) and rho(y, z)
    )
    is_antisymmetric = all(
        x == y
        for x in X for y in X
        if rho(x, y) and rho(y, x)
    )

    print(f"Множина X: {X}")
    print(f"Рефлексивність:{is_reflexive}")
    print(f"Транзитивність:{is_transitive}")
    print(f"Антисиметричність:{is_antisymmetric}")

    ipo = is_reflexive and is_transitive and is_antisymmetric
    print(f"\nЧи є відношенням порядку?{ipo}")
    print(f"Чи є ланцюгом?{ipo}")
    print(f"Чи є ґраткою?{ipo}")

    max_elem = max(X, key=lambda t: g(t))
    min_elem = min(X, key=lambda t: g(t))
    print(f"\nНайбільший (максимальний) елемент:{max_elem} (g({max_elem}) = {g(max_elem)})")
    print(f"Найменший (мінімальний) елемент:{min_elem} (g({min_elem}) = {g(min_elem)})")


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()