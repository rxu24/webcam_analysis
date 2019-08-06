import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_scatter(day, week_day):
    # Csv file analysis
    # Store the csv data into the dataframe starting from the third frame (header = 2)

    if (
            os.getcwd() != 'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + week_day + '/' + str(
            day)):
        os.chdir(
            'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + week_day + '/' + str(
                day))

    print('Current working directory: ' + os.getcwd())

    df = pd.read_csv(str(day) + '_outputDeepCut_resnet50_Project2Jul8shuffle1_125000.csv', header=2, index_col='coords')
    print(df)
    # print(type(df['bodyparts'][0])) # Read and print a dataframe using pandas library

    shoulder = df.iloc[:, [0, 1]]
    print(shoulder)

    elbow = df.iloc[:, [3, 4]]
    print(elbow)

    wrist = df.iloc[:, [6, 7]]
    print(wrist)

    hand = df.iloc[:, [9, 10]]
    print(hand)

    # Plot dataframes
    # shoulder.plot(kind='scatter', x='x', y='y', color='darkblue')
    ax = elbow.plot(kind='scatter', x='x.1', y='y.1', color='cyan', label='elbow')
    wrist.plot(kind='scatter', x='x.2', y='y.2', color='yellow', ax=ax, label='wrist')
    hand.plot(kind='scatter', x='x.3', y='y.3', color='red', ax=ax, label='hand')

    # Set domain and range for plot
    plt.ylim([0, 480])
    plt.xlim([0, 600])

    # Legend for graph
    plt.legend(loc='upper left')

    # Label title and axes
    plt.suptitle('Location of Body Parts in 2D Space')
    plt.xlabel('X position')
    plt.ylabel('Y position')

    # Display plot
    print('Press CTRL+C to stop showing plot.')
    plt.show()
