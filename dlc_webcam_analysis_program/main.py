import deeplabcut
import os
import numpy as np
from datetime import date
from video_functions import capture_video, play_video
from plot_scatter import plot_scatter

# Main function with code to run
if __name__ == "__main__":
    print('Beginning program...')
    print(os.getcwd())

    # Find the current day of the week
    my_date = date.today()
    day_of_week = my_date.strftime('%A')

    # Save a video input from the webcam
    capture_video(my_date, day_of_week)

    # Config Path
    config_path = 'D:/DeepLabCut/my_projects/Project2/config.yaml'
    video_path = (
            'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + day_of_week + '/' + str(
        my_date) + '/')
    # input('Please enter the directory of the video folder:')
    # 'C:Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + day_of_week + '/' + str(date)

    # Tensorflow cannot be running in other command prompt windows when running the following deeplabcut functions
    # Data used for DLC analysis comes from existing project data
    deeplabcut.analyze_videos(config_path, [video_path + 'output.avi'], save_as_csv=True)
    deeplabcut.create_labeled_video(config_path, [video_path + 'output.avi'], draw_skeleton=True,
                                    trailpoints=5)

    # Use OpenCV to play the labeled video created by deeplabcut
    # play_video(date, day_of_week)

    # Plot a scatter plot from the csv data of the video taken
    # At this point, current working directory is inside the file where the video and csv file are due to the change of directory in the capture_video function
    plot_scatter()

    # Other plotting methods
