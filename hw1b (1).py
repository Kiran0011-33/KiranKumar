import random

def one_step(x1, x2, x3):
    a1 = 0.5 * x1 * (x1 - 1) * x2
    a2 = x1 * x3 * (x3 - 1)      # already includes k2=2
    a3 = 3.0 * x2 * x3           # includes k3=3
    a0 = a1 + a2 + a3
    r = random.random() * a0
    if r < a1:
        return x1 - 2, x2 - 1, x3 + 4
    elif r < a1 + a2:
        return x1 - 1, x2 + 3, x3 - 2
    else:
        return x1 + 2, x2 - 1, x3 - 1

def solve_1b(N=200000, seed=1):
    random.seed(seed)
    xs1=[]; xs2=[]; xs3=[]
    for _ in range(N):
        x1,x2,x3 = 9,8,7
        for _ in range(7):
            x1,x2,x3 = one_step(x1,x2,x3)
        xs1.append(x1); xs2.append(x2); xs3.append(x3)

    def mean_var(arr):
        n=len(arr)
        m=sum(arr)/n
        v=sum((x-m)**2 for x in arr)/n
        return m,v

    m1,v1 = mean_var(xs1)
    m2,v2 = mean_var(xs2)
    m3,v3 = mean_var(xs3)

    print(f"E[X1]={m1:.6f}, Var(X1)={v1:.6f}")
    print(f"E[X2]={m2:.6f}, Var(X2)={v2:.6f}")
    print(f"E[X3]={m3:.6f}, Var(X3)={v3:.6f}")

if __name__ == "__main__":
    solve_1b()
