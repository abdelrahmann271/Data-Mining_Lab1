import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



#Importing csv file using pandas as a data frame.
df = pd.read_csv("wdbc.data",header=None)
print(df)

# plotting the graphs.

#1 Count plot.
plt.figure()
sns.countplot(x=1,data=df)

#2 Histogram plots.

#For all the features
# for i in range(2, 32):
#     plt.figure()
#     sns.histplot(data=df, x=i, hue=1)

#For some features

#plt.figure()
#sns.histplot(data=df, x=12,hue=1)
#plt.figure()
#sns.histplot(data=df, x=22,hue=1)


#4 Scatter Plot
plt.figure()
g = df[[i for i in range(2,12)]]
sns.pairplot(g)

#5 Correlation matrix
plt.figure()
f = df[[i for i in range(2,32)]]
sns.heatmap(f.corr(), vmin=-1, vmax=1)

#3 Box Plot.

#Applying normalization for the 30 features.
column = [i for i in range(2,32)]
df[column] = (df[column] - df[column].mean()) / df[column].std()
print(df)

# for i in range(2, 31):
#     plt.figure()
#     sns.boxplot(x=1, y=i , data=df)

plt.figure()
sns.boxplot(x=1, y=2 , data=df )


plt.show()
