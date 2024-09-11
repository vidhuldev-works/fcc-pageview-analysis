from time_series_visualizer import *

def main():

    # Print the first few rows of the filtered dataframe
    print('\nFiltered DataFrame:')
    print(clean_df(df).head())

    # Draw the line plot
    line_plot(df_filtered)

    # Draw the bar plot
    bar_plot(df_filtered)

    # Draw the box plots
    box_plot(df_filtered)

if __name__ == "__main__":
    main()