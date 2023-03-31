def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """Find the root of a function using the Newton-Raphson method.

    Parameters:
    f (function): The function whose root is to be found.
    df (function): The derivative of the function f.
    x0 (float): The initial guess for the root.
    tol (float): The tolerance for convergence (default=1e-6).
    max_iter (int): The maximum number of iterations (default=100).

    Returns:
    float: The root of the function f.
    """
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            return xn
        Dfxn = df(xn)
        if Dfxn == 0:
            raise ValueError("Newton-Raphson method failed: derivative is zero.")
        xn = xn - fxn / Dfxn
    raise ValueError("Newton-Raphson method failed to converge.")

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

x0 = 1.0
root = newton_raphson(f, df, x0)
print(root)  # prints 1.414213562373095
