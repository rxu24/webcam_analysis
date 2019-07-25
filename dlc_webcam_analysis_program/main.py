import deeplabcut
import os
import pandas as pd
import numpy as np
from datetime import date
from video_functions import capture_video, play_video

# Main function with code to run
if __name__ == "__main__":
    print('Beginning program...')

    # Find the current day of the week
    my_date = date.today()
    day_of_week = my_date.strftime('%A')

    # Config Path
    config_path = 'D:/DeepLabCut/my_projects/Project2/config.yaml'
    project_path = input('Please enter the directory of the project folder:')
    # 'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/'
    """
    # Save a video input from the webcam
    capture_video(day_of_week)

    # Tensorflow cannot be running in other command prompt windows when running the following deeplabcut functions
    # Data used for DLC analysis comes from existing project data
    deeplabcut.analyze_videos(config_path, [project_path + day_of_week + '_output.avi'], save_as_csv=True)
    deeplabcut.create_labeled_video(config_path, [project_path + day_of_week + '_output.avi'], draw_skeleton=True,
                                    trailpoints=5)

    # Use OpenCV to play the labeled video created by deeplabcut
    play_video(day_of_week)
    """
    # Csv file analysis
    df = pd.read_csv('Wednesday' + '_outputDeepCut_resnet50_Project2Jul8shuffle1_125000.csv', header=1, index_col='bodyparts')
    print(df)
    print(type(df['bodyparts'][0])) # Read and print a dataframe using pandas library