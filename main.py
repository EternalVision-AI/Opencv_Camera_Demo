import cv2
import socket
import struct
import pickle

# GStreamer pipeline for CSI camera
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        f"width=(int){capture_width}, height=(int){capture_height}, "
        f"format=(string)NV12, framerate=(fraction){framerate}/1 ! "
        "nvvidconv flip-method={flip_method} ! "
        "video/x-raw, format=(string)BGRx ! "
        "videoconvert ! "
        "appsink"
    )

# Configure socket for sending
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('195.201.199.101', 8080))  # IP and port of remote machine

# Open the CSI camera with OpenCV using GStreamer
cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Infinite loop to capture and send frames
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Encode frame as JPEG
    result, frame_encoded = cv2.imencode('.jpg', frame)

    # Serialize the frame
    data = pickle.dumps(frame_encoded, 0)
    size = len(data)

    # Send size of the frame first, then the actual frame
    client_socket.sendall(struct.pack(">L", size) + data)

cap.release()
client_socket.close()
