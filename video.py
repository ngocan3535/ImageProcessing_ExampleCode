import os
import cv2
import numpy as np

INPUT_VIDEO = 'cat.mp4'
OUTPUT_IMG = 'out_my_video'
os.makedirs(OUTPUT_IMG, exist_ok=True)

def print_image(img, frame_diff):
 new_img = np.zeros([img.shape[0], img.shape[1] * 2, img.shape[2]])  # [height,width * 2, channel]
 new_img[:, :img.shape[1], :] = img  # place color image on the left side
 new_img[:, img.shape[1]:, 0] = frame_diff  # place gray image on the right side
 new_img[:, img.shape[1]:, 1] = frame_diff
 new_img[:, img.shape[1]:, 2] = frame_diff
 return new_img

def main(video_path):
 cap = cv2.VideoCapture(video_path) #https://docs.opencv.org/4.0.0/d8/dfe/classcv_1_1VideoCapture.html
 last_gray = None
 idx = -1
 while (True):
     ret, frame = cap.read()  # read frames
     idx += 1
     if not ret:
         print('Stopped reading the video (%s)' % video_path)
     break
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert color image to gray
     if last_gray is None:
         last_gray = gray
         continue
     diff = cv2.absdiff(gray,last_gray)  # frame difference!https: // docs.opencv.org / 4.0.0 / d2 / de8 / group__core__array.html  # ga6fef31bc8c4071cbc114a758# a2b79c14
     cv2.imwrite(os.path.join(OUTPUT_IMG, 'img_%06d.jpg' % idx),print_image(frame, diff))
     last_gray = gray
     print('Done image @ %d...' % idx)
     pass
 pass
if __name__ == "__main__":
 print('Running frame difference algorithm on %s' % INPUT_VIDEO)
 main(video_path=INPUT_VIDEO)
 # print('ffmpeg -framerate 24 -f image2 -start_number 1 -i out_my_video/img_%*.jpg -crf 10 -q:v 5  -pix_fmt yuv420p out_video.mp4')
