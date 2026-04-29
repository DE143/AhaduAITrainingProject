#  Plot and Explore Various Distributions
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import skew, kurtosis
# Generate random data from different distributions
data_normal = np.random.normal(loc=0, scale=1, size=1000)
data_uniform = np.random.uniform(low=0, high=1, size=1000)
data_exponential = np.random.exponential(scale=1, size=1000)
# Plot histograms and KDEs
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.hist(data_normal, bins=30, density=True)
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")

plt.subplot(1, 3, 2)
plt.hist(data_uniform, bins=30, density=True)
plt.title("Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Density")

plt.subplot(1, 3, 3)
plt.hist(data_exponential, bins=30, density=True)
plt.title("Exponential Distribution")
plt.xlabel("Value")
plt.ylabel("Density")

plt.tight_layout()
plt.show()

