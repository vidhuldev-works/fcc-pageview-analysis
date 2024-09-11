import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")
df_filtered = pd.read_csv("filtered-fcc-forum-pageviews.csv", index_col="date")

# Function to filter the data by excluding the top and bottom 2.5%
def clean_df(dataframe):
    # Calculate the 2.5% and 97.5% quantiles
    lower_quantile = dataframe['value'].quantile(0.025)
    upper_quantile = dataframe['value'].quantile(0.975)

    # Filter the dataframe to exclude values outside the quantiles
    filtered_df = dataframe[(dataframe['value'] >= lower_quantile) & (dataframe['value'] <= upper_quantile)]

    # Save the filtered dataframe to a new file
    filtered_df.to_csv("filtered-fcc-forum-pageviews.csv")

    # Return the filtered dataframe
    return filtered_df

# Function to draw a line plot of the filtered dataframe
def line_plot(dataframe):
    # Set the figure size
    plt.figure(figsize=(10, 5))

    # Plot the data
    plt.plot(dataframe.index, dataframe['value'], color='gold', linewidth=1)

    # Set the title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Show the plot
    plt.show()

# Convert the date column to datetime and extract year and month
df_filtered.reset_index(inplace=True)
df_filtered['date'] = pd.to_datetime(df_filtered['date'])
df_filtered['year'] = df_filtered['date'].dt.year
df_filtered['month'] = df_filtered['date'].dt.month

# Function to draw a bar plot of the filtered dataframe
def bar_plot(dataframe):
    # Group the dataframe by year and month, then calculate the mean
    grouped_df = dataframe.groupby(['year', 'month']).mean().reset_index()

    # Pivot the dataframe to have years as rows and months as columns
    pivot_df = grouped_df.pivot(index='year', columns='month', values='value')

    # Plot the data
    pivot_df.plot(kind='bar', figsize=(10, 6))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views per Month')
    plt.legend(title='Months')

    # Show the plot
    plt.show()

# Function to draw box plots of the filtered dataframe
def box_plot(dataframe):
    # Create a figure with two subplots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

    # Year-wise box plot
    sns.boxenplot(x='year', y='value', data=dataframe, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxenplot(x='month', y='value', data=dataframe, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plots
    plt.show()