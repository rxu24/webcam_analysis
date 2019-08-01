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

    ### Read csv data into dataframe ###
    # Streamline later by calling plot_scatter() function, stop the "hard coding"
    df = pd.read_csv('outputDeepCut_resnet50_Project2Jul8shuffle1_125000.csv', header=2, index_col='coords')
    shoulder = df.iloc[:, [0, 1]]
    elbow = df.iloc[:, [3, 4]]
    wrist = df.iloc[:, [6, 7]]
    hand = df.iloc[:, [9, 10]]

    print('CSV data successfully saved into panda Dataframes!')

    ### Save video as individual frames (PNG format) ###
    # Check to see if video_file exists
    try:
        video_file = cv2.VideoCapture(video_path + 'outputDeepCut_resnet50_Project2Jul8shuffle1_125000_labeled.mp4')
    except:
        print('Video file not found!')

    # Create a directory to store the png images that will be extracted from the video_file
    if os.path.exists(
            'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + week_day + '/' + str(
                    day) + '/output_video_frames'):
        os.chdir(
            'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + week_day + '/' + str(
                day) + '/output_video_frames')
    else:
        os.mkdir('output_video_frames')
        os.chdir(
            'C:/Users/ruidi/OneDrive/Documents/GitProjects/webcam_analysis/dlc_webcam_analysis_program/' + week_day + '/' + str(
                day) + '/output_video_frames')

    # Calculate frame rate and total number of frames of video
    frame_rate = video_file.get(cv2.CAP_PROP_FPS)
    total_frames = int(video_file.get(cv2.CAP_PROP_FRAME_COUNT))

    print('Frame rate: ' + str(frame_rate))
    print('Total frames in video: ' + str(total_frames))

    ret, image = video_file.read()

    counter = 0
    while (ret==True):
        cv2.imwrite("frame%d.PNG" % counter, image)  # save frame as PNG file
        ret, image = video_file.read()
        print('Read a new frame: ', ret)
        counter += 1

    ### Plotting section ###
    plt.figure(1)
    plt.show()

    # Iterate through all the frames of the video, plot both the picture and the data points using subplot
    count = 0
    while (count < total_frames):
        # plt.subplot(211)
        # cv2.imshow('Labeled video frame by frame', image)

        print('Frame #: ' + str(count))
        print('Elbow location: (' + str(elbow.iloc[count, 0]) + ', ' + str(elbow.iloc[count, 1]) + ')')
        print('Wrist location: (' + str(wrist.iloc[count, 0]) + ', ' + str(wrist.iloc[count, 1]) + ')')
        print('Hand location: (' + str(hand.iloc[count, 0]) + ', ' + str(hand.iloc[count, 1]) + ')')

        # plt.subplot(212)
        # plt.plot(elbow.iloc[count,0], elbow.iloc[count,1], color='cyan',  label='elbow')
        # plt.plot(wrist.iloc[count,0], wrist.iloc[count,1], color='yellow', label='wrist')
        # plt.plot(hand.iloc[count,0], hand.iloc[count,1], color = 'red', label='hand')

        count = count + 1

    video_file.release()
    cv2.destroyAllWindows()
