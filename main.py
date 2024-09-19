import cv2

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

# Open the CSI camera with OpenCV using GStreamer
cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera. Check GStreamer pipeline and camera connection.")
    exit()

# Capture and process frames
count = 0
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame. Check camera and pipeline.")
        break

    print("Frames: ", count)
    # Process the frame (e.g., save to file or perform analysis)
    # Uncomment below line if you want to save frames to disk for testing
    # cv2.imwrite('frame.jpg', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    count += 1

cap.release()
cv2.destroyAllWindows()
