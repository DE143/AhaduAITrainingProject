#  mean, Median, Mode

data = [20,10,30,1,40,50,60,70,80,90,100]
mean = sum(data)/len(data)
print("Mean:", mean)
sorted_data = sorted(data)
n = len(data)
if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]
print("Median:", median)
from collections import Counter
data_count = Counter(data)  
mode = data_count.most_common(1)[0][0]
print("Mode:", mode)



#  confidence interval
from dbm import error
import math
import scipy.stats as stats
data = [20,10,30,1,40,50,60,70,80,90,100]
mean = sum(data)/len(data)
std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / (len(data) - 1))
confidence_level = 0.95
z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)
margin_of_error = z_score * (std_dev / math.sqrt(len(data)))
confidence_interval = (mean - margin_of_error, mean + margin_of_error)
print("Confidence Interval:", confidence_interval)

#  statistical significance
import scipy.stats as stats
data1 = [20,10,30,1,40]
data2 = [50,60,70,80,90]
t_statistic, p_value = stats.ttest_ind(data1, data2)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. The difference is statistically significant.")
else:    
    print("Fail to reject the null hypothesis. The difference is not statistically significant.")



# mean squared error and root mean squared error
import numpy as np
y_true = [3, -0.5, 2, 10]
y_pred = [2.5, 0, 2.5, 11]
mse = np.mean((np.array(y_true) - np.array(y_pred)) ** 2)
print("Mean Squared Error:", mse)
rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)

# linear regression
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
denominator = sum((x[i] - x_mean) ** 2 for i in range
(n))
slope = numerator / denominator
intercept = y_mean - slope * x_mean
print("Slope:", slope)


#  task 3: calculate evaluation matrics
def mean_squared_error(y_true, y_pred):
    return np.mean((np.array(y_true) - np.array(y_pred)) ** 2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((np.array(y_true) - np.array(y_pred)) ** 2)
    ss_tot = np.sum((np.array(y_true) - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)


# generate synthetics data
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.rand(100) * 10
y = 2.5 * x + np.random.randn(100) * 5
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Synthetic Data')
plt.show()
