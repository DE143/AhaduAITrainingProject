import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#basic plot
# a = np.linspace(0, 10, 100)
# b = np.sin(a)
# x= [1, 2, 3, 4, 5]
# y= [2, 4, 6, 8, 10]
# plt.plot(x, y, label="Dawit")
# plt.plot(a, b, label="Sine Wave")
# plt.title('Matplotlib Sample')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.legend()
# plt.grid()
# plt.show()



# bar chart
# name = ['Abebe', 'Belay', 'Chala', 'Demelash', 'Etsube']
# accountBalance = [10000, 20000, 15000, 25000, 30000]
# plt.bar(name, accountBalance, color='red')
# plt.title('Customer Account Balance')
# plt.xlabel('Customers')
# plt.ylabel('Account Balance')
# plt.show()

# pie chart
# labels = ['Abebe', 'Belay', 'Chala', 'Demelash', 'Etsube']
# sizes = [10000, 20000, 15000, 25000, 30000]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.title('Customer Account Balance Distribution')
# plt.axis('equal')
# plt.show()




# data = {
#     'Name': ['Abebe', 'Belay', 'Chala', 'Demelash', 'Etsube'],
#     'age': [75, 30, 35, 40, 45],
#     'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#     'address': ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Jimma', 'Dessie'],
#     'AccountBalance': [10000, 20000, 15000, 25000, 30000],
# }
# df = pd.DataFrame(data)
# groupdf = df.groupby('gender')['AccountBalance'].sum().reset_index()
# plt.bar(groupdf['gender'], groupdf['AccountBalance'], color='red')
# plt.title('Customer Account Balance Distribution by Gender')
# plt.xlabel('Gender')
# plt.ylabel('Account Balance')
# plt.show()


#  Histogram
# data = {
#     'Name': ['Abebe', 'Belay', 'Chala', 'Demelash', 'Etsube'],
#     'age': [75, 30, 35, 40, 45],
#     'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#     'address': ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Jimma', 'Dessie'],
#     'AccountBalance': [10000, 20000, 15000, 25000, 30000],
#     }
# df = pd.DataFrame(data)
# plt.hist(df['gender'], bins=2, color='blue', edgecolor='black')
# plt.title('Gender Distribution')
# plt.xlabel('Gender')
# plt.ylabel('Frequency')
# plt.show()



# scatter plot
# data = {
#     'Name': ['Abebe', 'Belay', 'Chala', 'Demelash', 'Etsube'],
#     'age': [75, 30, 35, 40, 45],
#     'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#     'address': ['Addis Ababa', 'Bahir Dar', 'Gond ar', 'Jimma', 'Dessie'],
#     'AccountBalance': [10000, 20000, 15000, 25000, 30000],
# }
# df = pd.DataFrame(data)
# plt.scatter(df['age'], df['AccountBalance'], color='green')
# plt.title('Age vs Account Balance')
# plt.xlabel('Age')
# plt.ylabel('Account Balance')
# plt.show()

# seaborn
import seaborn as sns
data = {
    'Name': ['Abebe', 'Belay', 'Chala', 'Demelash', 'Etsube'],
    'age': [75, 30, 35, 40, 45],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'address': ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Jimma', 'Dessie'],
    'AccountBalance': [10000, 20000, 15000, 25000, 30000],
}
df = pd.DataFrame(data)
sns.barplot(x='gender', y='AccountBalance', data=df, palette='viridis')
plt.title('Customer Account Balance Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Account Balance')
plt.show()
