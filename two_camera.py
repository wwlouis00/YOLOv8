#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

if not cap2.isOpened():
    print("Cannot open camera")
    exit()

#cv2.namedWindow("live", cv2.WINDOW_AUTOSIZE); # 命名一個視窗，可不寫
while(True):
    # 擷取影像
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if not ret2:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 彩色轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # 顯示圖片
    cv2.imshow('live', frame)
    cv2.imshow('live2', frame2)
    #cv2.imshow('live', gray)

    # 按下 q 鍵離開迴圈
    if cv2.waitKey(1) == ord('q'):
        break

# 釋放該攝影機裝置
cap.release()
cap2.release()
cv2.destroyAllWindows()