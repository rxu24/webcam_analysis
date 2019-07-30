import deeplabcut
import os
import pandas as pd
import numpy as np
from datetime import date
from video_functions import capture_video, play_video
import matplotlib.pyplot as plt

# Main function with code to run
if __name__ == "__main__":
    print('Beginning program...')
    # print(os.getcwd())

    # Find the current day of the week
    my_date = date.today()
    day_of_week = my_date.strftime('%A')

    # Save a video input from the webcam
    capture_video(my_date, day_of_week)

    # Config Path
    config_path = 'D:/DeepLabCut/my_projects/Project2/config.yaml'
    video_path = ('C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + day_of_week + '/' + str(my_date) + '/')
    # input('Please enter the directory of the video folder:')
    # 'C:Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + day_of_week + '/' + str(date)

    # Tensorflow cannot be running in other command prompt windows when running the following deeplabcut functions
    # Data used for DLC analysis comes from existing project data
    deeplabcut.analyze_videos(config_path, [video_path + 'output.avi'], save_as_csv=True)
    deeplabcut.create_labeled_video(config_path, [video_path + 'output.avi'], draw_skeleton=True,
                                    trailpoints=5)

    # Use OpenCV to play the labeled video created by deeplabcut
    #play_video(date, day_of_week)

    # Csv file analysis
    # Store the csv data into the dataframe starting from the third frame (header = 2)
    df = pd.read_csv('outputDeepCut_resnet50_Project2Jul8shuffle1_125000.csv', header=2, index_col='coords')
    print(df)
    #print(type(df['bodyparts'][0])) # Read and print a dataframe using pandas library

    shoulder = df.iloc[:,[0,1]]
    print(shoulder)

    elbow = df.iloc[:,[3,4]]
    print(elbow)

    wrist = df.iloc[:,[6,7]]
    print(wrist)
    
    hand = df.iloc[:,[9,10]]
    print(hand)

    # Plot dataframes
    #shoulder.plot(kind='scatter', x='x', y='y', color='darkblue')
    ax = elbow.plot(kind='scatter', x='x.1', y='y.1', color='cyan', label='elbow')
    wrist.plot(kind='scatter', x='x.2', y='y.2', color='yellow', ax=ax, label='wrist')
    hand.plot(kind='scatter', x='x.3', y='y.3', color='red', ax=ax, label='hand')

    # Set domain and range for plot
    plt.ylim([0,480])
    plt.xlim([0,600])

    # Legend for graph
    plt.legend(loc= 'upper left')

    # Label title and axes
    plt.suptitle('Location of Body Parts in 2D Space')
    plt.xlabel('X position')
    plt.ylabel('Y position')

    #Display plot
    plt.show()