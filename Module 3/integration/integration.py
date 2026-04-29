# import sympy as sp
# def calculate_integral(func, var):
#     indefinite_integral = sp.integrate(func, var)
#     definite_integral = sp.integrate(func, (var, 0, 1))
#     return indefinite_integral, definite_integral



# x = sp.symbols('x')
# func=2*x**2+x+1
# indefinite, definite = calculate_integral(func, x)
# print(f"Indefinite Integral: {indefinite}")
# print(f"Definite Integral: {definite}")




# implement stochastic gradient descent for a linear model
import numpy as np
def stochastic_gradient_descent(X, y, learning_rate=0.01, epochs=100):
    m, n = X.shape
    theta = np.zeros(n)
    
    for epoch in range(epochs):
        for i in range(m):
            xi = X[i]
            yi = y[i]
            prediction = np.dot(xi, theta)
            error = prediction - yi
            gradient = xi * error
            theta -= learning_rate * gradient
            
    return theta


# number of samples
m = int(input("Enter number of samples: "))

# number of features per sample
n = int(input("Enter number of features per sample: "))

# input X
X = []
for i in range(m):
    row = list(map(float, input(f"Enter features for sample {i+1} (comma separated): ").split(',')))
    
    if len(row) != n:
        print("Error: number of features must match n")
        exit()
    
    X.append(row)

X = np.array(X)

# input y
y = np.array(list(map(float, input("Enter target values (comma separated): ").split(','))))

# check size match
if len(y) != m:
    print("Error: number of target values must match number of samples")
    exit()

theta = stochastic_gradient_descent(X, y)

print(f"Optimized Parameters: {theta}")


# visualization 
import matplotlib.pyplot as plt 

plt.scatter(X[:, 0], y, color='blue', label='Data Points')
x_line = np.linspace(min(X[:, 0]), max(X[:, 0]), 100)
y_line = theta[0] * x_line + theta[1]
plt.plot(x_line, y_line, color='red', label='Fitted Line')
plt.xlabel('Feature 1')
plt.i ('Target')
plt.title('Stochastic Gradient Descent Linear Fit')
plt.legend()
plt.show()
