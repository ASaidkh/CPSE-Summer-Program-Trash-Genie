import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import servo
import time
import torch

cap=cv2.VideoCapture(1)

servo.center()
#Load YOLOv5 Model, third parameter is the path to the weights
model = torch.hub.load("ultralytics/yolov5","custom","SmallModel.pt")
count =0
while True: 
    
    ret,frame = cap.read() 
    count+=1
    #Takes one of every 5 frames
    if count%5==0:
    
        frame=cv2.resize(frame,(1080,720))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #Processes the image frame with YOLOv5 Model
        pred = model(frame)
        
        #If an object is detected above 70% confidence, dump
        if len(pred.pandas().xyxy[0]['confidence']) > 0 :
            predInd = pred.pandas().xyxy[0]['confidence'].argmax()
            print(f"Class = {pred.pandas().xyxy[0]['name'][predInd]} Confidence = {pred.pandas().xyxy[0]['confidence'][predInd]}")
            if pred.pandas().xyxy[0]['confidence'][predInd]>0.7:
                servo.dump(pred.pandas().xyxy[0]['name'][predInd].upper())

    
    
    
cap.release()
