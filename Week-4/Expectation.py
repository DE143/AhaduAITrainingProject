import numpy as np
# expection, variance, standard deviation
# 1. expection
data =np.array([1, 2, 3, 4, 5, 6])
probability = np.array([1/6] * 6)
expectation = np.sum(data * probability)
print("Expectation:", expectation)
# 2. variance
variance = np.sum(probability * (data - expectation) ** 2)
print("Variance:", variance)
# 3. standard deviation
std_deviation = np.sqrt(variance)
print("Standard Deviation:", std_deviation)