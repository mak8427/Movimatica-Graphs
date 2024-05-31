Position Data Analysis

This project is designed to analyze position data from a CSV file. The data includes timestamped records of positions along with additional information such as velocity, address, city, and more. The main goal of this analysis is to determine the most frequent time of response, visualize the distribution of response times, and analyze the time spent at various addresses.
Features

    Data Loading and Preprocessing
        Load the data from a CSV file.
        Rename the columns for better readability.
        Convert the date column to a datetime object.

    Mean Time of Refresh for the Position
        Calculate the time differences between consecutive records.
        Filter out the time differences that are less than 2 seconds or more than 15 minutes.
        Calculate and print the most frequent time of response, minimum time, maximum time, and average time of response.
        Visualize the distribution of response times using histograms and violin plots.

    Time Spent at Each Address
        Determine the amount of time spent at each address.
        Sort and display the top 10 addresses where the most time was spent.
        Visualize the time spent at these addresses using a bar chart.
