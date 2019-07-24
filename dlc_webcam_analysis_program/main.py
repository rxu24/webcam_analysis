import deeplabcut
import tensorflow as tf
import os
import pandas as pd
import numpy as np
import cv2
from datetime import date


# Read and store video input from webcam
def capture_video():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Change the name of the output later to be a concatenation of date or day of week and 'output'
    out = cv2.VideoWriter(day_of_week + '_output.avi', fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:

            cv2.flip(frame, 1)
            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)

            # specify a key that will turn off camera; currently using spacebar
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break
        else:
            break

    # Release everything
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def play_video():  # does not work currently
    cap = cv2.VideoCapture(
        'C:/Users/ruidi/PycharmProjects/dlc_webcam_analysis_program/' + 'Monday' + 'outputDeepCut_resnet50_Project2Jul8shuffle125000_labeled.mp4')

    if (cap.isOpened() == False):
        print('Error opening video file!')

    while (cap.isOpened()):
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()


# Main function with code to run
if __name__ == "__main__":
    print('Beginning program...')

    # Find the current day of the week
    my_date = date.today()
    day_of_week = my_date.strftime('%A')

    # Config Path
    config_path = 'D:/DeepLabCut/my_projects/Project2/config.yaml'
    project_path = input('Please enter the directory of the project folder:')
        #'C:/Users/ruidi/PycharmProjects/dlc_webcam_analysis_program/'

    capture_video()

    # Tensorflow cannot be running in other command prompt windows when running the following deeplabcut functions
    # Data used for DLC analysis comes from existing project data
    deeplabcut.analyze_videos(config_path, [project_path + day_of_week + '_output.avi'])

    deeplabcut.create_labeled_video(config_path, [project_path + day_of_week + '_output.avi'], draw_skeleton=True,
                                    trailpoints=5)

    # Use OpenCV to play the labeled video created by deeplabcut
    play_video()
