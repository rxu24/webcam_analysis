import deeplabcut
import cv2


# Read and store video input from webcam
def capture_video(day_of_week):
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


def play_video(day_of_week):  # does not work currently
    cap = cv2.VideoCapture(
        'C:/Users/ruidi/PycharmProjects/dlc_webcam_analysis_program/' + day_of_week + 'outputDeepCut_resnet50_Project2Jul8shuffle125000_labeled.mp4')

    if (cap.isOpened() == False):
        print('Error opening video file!')

    while (cap.isOpened()):
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()