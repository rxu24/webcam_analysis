import os
import numpy as np
import cv2


# Use 'day' and 'week_day' variables for functions
# Read and store video input from webcam
def capture_video(day, week_day):
    print('Running capture_video() function now...')
    # Directory to store videos
    # print(os.path.exists(day_of_week + '/' + str(date)))
    if (os.path.exists(week_day + '/' + str(day))):
        os.chdir(week_day + '/' + str(day))
    else:
        os.makedirs(week_day + '/' + str(day))
        os.chdir(week_day + '/' + str(day))

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Change the name of the output later to be a concatenation of date or day of week and 'output'
    out = cv2.VideoWriter(str(day) + '_output.avi', fourcc, 20.0, (640, 480), isColor = True)

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:

            # flip frame
            cv2.flip(frame, 1)

            # write the flipped frame
            out.write(frame) # Write the normal frame

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


def mask_video(day, week_day, video_path):
    print('Running mask_video() function...')

    if (os.path.exists(week_day + '/' + str(day))):
        os.chdir(week_day + '/' + str(day))
    else:
        os.makedirs(week_day + '/' + str(day))
        os.chdir(week_day + '/' + str(day))

    video_file = cv2.VideoCapture(video_path + str(day) + '_output.avi')

    if (os.path.exists(video_path + str(day) + '_output.avi')):
        print('Video found')
    else:
        print('No video found at specified directory location!')

    if (video_file.isOpened() == False):
        print('Error opening video file!')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Change the name of the output later to be a concatenation of date or day of week and 'output'
    out = cv2.VideoWriter(str(day) + '_output_subtracted.avi', fourcc, 20.0, (640, 480), isColor=False)
    fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

    while (video_file.isOpened()):
        ret, frame = video_file.read()

        if ret == True:

            fgmask = fgbg.apply(frame)  # Apply background subtraction to the frame

            # out.write(frame) # Write the normal frame
            out.write(fgmask)  # Write the frame with the background subtraction applied

            # cv2.imshow('frame', frame)
            cv2.imshow('frame', fgmask)  # Show the frame with the background subtraction applied

            if cv2.waitKey(20) & 0xFF == ord(' '):
                break
        else:
            break

    # Release everything
    video_file.release()
    out.release()
    cv2.destroyAllWindows()


def play_video(day, week_day, video_path):
    print('Running play_video() function now...')

    video_file = cv2.VideoCapture(
        video_path + str(day) + '_outputDeepCut_resnet50_Project2Jul8shuffle1_125000_labeled.mp4') # requires deeplabcut analysis prior

    if (os.path.exists(video_path + str(day) + '_outputDeepCut_resnet50_Project2Jul8shuffle1_125000_labeled.mp4')):
        print('Video found')
    else:
        print('No video found at specified directory location!')

    if (video_file.isOpened() == False):
        print('Error opening video file!')

    while (video_file.isOpened()):
        ret, frame = video_file.read()

        if ret == True:
            cv2.imshow(week_day + '/' + str(day) + '/output',
                       frame)  # is this the path of video? may need to be changed...

            if cv2.waitKey(25) & 0xFF == ord(' '):
                break
        else:
            break

    video_file.release()
    cv2.destroyAllWindows()
