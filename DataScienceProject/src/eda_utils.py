"""Utility functions for exploratory data analysis."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    """Load insurance claims dataset."""
    return pd.read_csv(filepath)


def basic_info(df):
    """Display basic information about the dataset."""
    print("Dataset Shape:", df.shape)
    print("\nColumn Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nBasic Statistics:")
    print(df.describe())


def plot_distribution(df, column, title=None):
    """Plot distribution of a numerical column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(title or f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.tight_layout()
    return plt


def plot_categorical(df, column, title=None):
    """Plot count of categorical column."""
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='bar')
    plt.title(title or f'Count of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt


def correlation_analysis(df, numerical_cols):
    """Generate correlation matrix for numerical columns."""
    plt.figure(figsize=(12, 8))
    correlation = df[numerical_cols].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    return plt, correlation
