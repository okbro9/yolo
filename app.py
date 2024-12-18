import cv2
import cvzone
from ultralytics import YOLO
import math
import statistics
import streamlit as st
import time

# Title and description for the Streamlit app
st.title("Real-time Object Detection with YOLOv8")
st.text("Using a webcam feed")

# Streamlit widget to select source: webcam or video
source = st.sidebar.selectbox("Select input source", ["Webcam", "Video"])
