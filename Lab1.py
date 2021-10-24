import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Importing csv file using pandas as a data frame
df = pd.read_csv("wdbc.data", header=None)
# print(df)


# Plotting the graphs
# 1 Count plot.
def count_plot():
    plt.figure()
    sns.countplot(x=1, data=df)
    plt.show()


# 2 Histogram plots.
def histogram():
    # For all the features
    feature_no = 3
    for z in range(3):
        fig_hist, axs = plt.subplots(2, 5)
        start, end_of_row = 0, 5
        for i in range(0, 5):
            sns.histplot(data=df, x=feature_no - 1, hue=1, ax=axs[0, i])
            axs[0, i].set(xlabel=f'feature {feature_no}')
            feature_no = feature_no + 1

        for i in range(start, end_of_row):
            sns.histplot(data=df, x=feature_no - 1, hue=1, ax=axs[1, i])
            axs[1, i].set(xlabel=f'feature {feature_no}')
            feature_no = feature_no + 1
    plt.show()


# 3 Box Plot.
def box_plot():
    # Applying normalization for the 30 features.
    column = [i for i in range(2, 32)]
    df[column] = (df[column] - df[column].mean()) / df[column].std()
    print(df)

    # Box plot for all features..
    # Individually ..
    # for i in range(2, 31):
    #     plt.figure()
    #     sns.boxplot(x=1, y=i , data=df)

    fig, axes = plt.subplots(5, 6, figsize=(20, 20))
    cnt = 2
    for i in range(0, 5):
        for j in range(0, 6):
            sns.boxplot(ax=axes[i, j], x=1, y=cnt, data=df)
            axes[i][j].set_title(cnt)
            cnt = cnt + 1
    plt.show()


# 4 Scatter Plot for mean features.
def scatter():
    g = df[[i for i in range(2, 12)]]
    sns.pairplot(g)

    # Scatter Plot for SE features.
    g = df[[i for i in range(12, 22)]]
    sns.pairplot(g)

    # Scatter Plot for worst features.
    g = df[[i for i in range(22, 32)]]
    sns.pairplot(g)
    plt.show()


# 5 Correlation matrix
def correlate_matrix():
    plt.figure()
    f = df[[i for i in range(2, 32)]]
    sns.heatmap(f.corr(), vmin=-1, vmax=1)
    plt.show()


def main():
    count_plot()


if __name__ == "__main__":
    main()
