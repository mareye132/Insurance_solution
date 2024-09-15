import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Insurance_analysis:
    def __init__(self, data_path, delimiter=','):
        self.df = pd.read_csv(data_path, delimiter=delimiter)

    def data_summary(self):
        return self.df.describe(include='all')

    def data_structure(self):
        return self.df.info()

    def check_missing_values(self):
        return self.df.isnull().sum()

    def get_variance(self, column_name):
        return self.df[column_name].var()

    def get_std_deviation(self, column_name):
        return self.df[column_name].std()

    def plot_histogram(self, column_name):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[column_name].dropna(), bins=30, kde=True)
        plt.title(f'Histogram of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.show()

    def plot_bar_chart(self, column_name):
        plt.figure(figsize=(12, 6))
        self.df[column_name].value_counts().plot(kind='bar')
        plt.title(f'Bar Chart of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.show()

    def scatter_plot(self, x_column, y_column):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x=x_column, y=y_column)
        plt.title(f'Scatter Plot of {x_column} vs {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()

    def correlation_matrix(self):
        """Generate a correlation matrix"""
        # Select numeric columns only
        numeric_df = self.df.select_dtypes(include='number')
        corr = numeric_df.corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title('Correlation Matrix')
        plt.show()

    def geographical_trend_comparison(self, location_column, value_column):
        plt.figure(figsize=(12, 6))
        self.df.groupby(location_column)[value_column].mean().plot(kind='bar')
        plt.title(f'Geographical Trend Comparison of {value_column} by {location_column}')
        plt.xlabel(location_column)
        plt.ylabel(f'Average {value_column}')
        plt.show()

    def outlier_detection(self, column_name):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.df[column_name])
        plt.title(f'Outlier Detection for {column_name}')
        plt.xlabel(column_name)
        plt.show()
