import cv2
import pandas as pd
import matplotlib.pyplot as plt
import os

def comparison_plot(date, day_of_week, video_path):

    video_file = cv2.VideoCapture(video_path + 'outputDeepCut_resnet50_Project2Jul8shuffle1_125000_labeled.mp4')
    frame_rate = video_file.get(cv2.CAP_PROP_FPS)
    total_frames = int(video_file.get(cv2.CAP_PROP_FRAME_COUNT))


    video_file.release()
    cv2.destroyAllWindows()