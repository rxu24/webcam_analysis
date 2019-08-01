import cv2
import pandas as pd
import matplotlib.pyplot as plt
import os

def comparison_plot(day, week_day, video_path):

    if (
            os.getcwd() != 'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + week_day + '/' + str(
            day)):
        os.chdir(
            'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + week_day + '/' + str(
                day))

    print(os.getcwd())

    video_file = cv2.VideoCapture(video_path + 'outputDeepCut_resnet50_Project2Jul8shuffle1_125000_labeled.mp4')

    frame_rate = video_file.get(cv2.CAP_PROP_FPS)
    total_frames = int(video_file.get(cv2.CAP_PROP_FRAME_COUNT))

    print('Frame rate: ' + str(frame_rate))
    print('Total frames in video: ' + str(total_frames))

    ret, image = video_file.read()

    # Read csv data into dataframe
    # Streamline later by calling plot_scatter() function, stop the "hard coding"
    df = pd.read_csv('outputDeepCut_resnet50_Project2Jul8shuffle1_125000.csv', header=2, index_col='coords')
    shoulder = df.iloc[:, [0, 1]]
    elbow = df.iloc[:, [3, 4]]
    wrist = df.iloc[:, [6, 7]]
    hand = df.iloc[:, [9, 10]]

    print('CSV data successfully saved into panda Dataframes!')

    count = 0
    plt.figure(1)

    while (count < total_frames):
        #plt.subplot(211)
        #cv2.imshow('Labeled video frame by frame', image)

        print('Frame #: ' + str(count))
        print('Elbow location: (' + str(elbow.iloc[count,0])+ ', ' + str(elbow.iloc[count,1]) + ')')
        print('Wrist location: (' + str(wrist.iloc[count, 0]) + ', ' + str(wrist.iloc[count, 1]) + ')')
        print('Hand location: (' + str(hand.iloc[count, 0]) + ', ' + str(hand.iloc[count, 1]) + ')')
        #plt.subplot(212)
        #plt.plot(elbow.iloc[count,0], elbow.iloc[count,1], color='cyan',  label='elbow')
        #plt.plot(wrist.iloc[count,0], wrist.iloc[count,1], color='yellow', label='wrist')
        #plt.plot(hand.iloc[count,0], hand.iloc[count,1], color = 'red', label='hand')

        count = count + 1


    video_file.release()
    cv2.destroyAllWindows()