import deeplabcut
import os
from datetime import date
from video_functions import capture_video, play_video, mask_video
from comparison_plot import comparison_plot
from plot_scatter import plot_scatter

# Main function with code to run
# Use my_date and day_of_week variables within main
if __name__ == "__main__":
    print('Beginning program...')
    print(os.getcwd())

    # Find the current day of the week
    my_date = date.today()
    day_of_week = my_date.strftime('%A')

    # Save a video input from the webcam
    #capture_video(my_date, day_of_week)

    # Config Path
    config_path = 'D:/DeepLabCut/my_projects/dlc_webcam_analysis/config.yaml'
    video_path = (
            'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + day_of_week + '/' + str(
        my_date) + '/')
    # input('Please enter the directory of the video folder:')
    # 'C:Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + day_of_week + '/' + str(date)

    # Tensorflow cannot be running in other command prompt windows when running the following deeplabcut functions
    # Data used for DLC analysis comes from existing project data
    # Saving as CSV must be True in order to execute plotting functions later!
    #deeplabcut.analyze_videos(config_path, [video_path + str(my_date) + '_output.avi'], save_as_csv=True)
    #deeplabcut.create_labeled_video(config_path, [video_path + str(my_date) + '_output.avi'], draw_skeleton=True, trailpoints=5)

    # Use OpenCV to play the labeled video created by deeplabcut
    #mask_video(my_date, day_of_week, video_path)
    #play_video(my_date, day_of_week, video_path)

    # Plot a scatter plot from the csv data of the video taken
    # At this point, current working directory is inside the file where the video and csv file are due to the change of directory in the capture_video function
    #plot_scatter(my_date, day_of_week, str(my_date) + '_outputDeepCut_resnet50_dlc_webcam_analysisAug5shuffle1_435000.csv')

    # Other plotting methods
    comparison_plot(my_date, day_of_week, video_path)

    ### BEGIN TESTING OF BACKGROUND SUBTRACTION! ###
    #deeplabcut.analyze_videos(config_path, [video_path + str(my_date) + '_output_subtracted.avi'], save_as_csv=True)
    #deeplabcut.create_labeled_video(config_path, [video_path + str(my_date) + '_output_subtracted.avi'], draw_skeleton=True, trailpoints=5)
    #plot_scatter(my_date, day_of_week, str(my_date) + '_output_subtractedDeepCut_resnet50_dlc_webcam_analysisAug5shuffle1_435000.csv')