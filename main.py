import cv2
import subprocess

def start_camera_stream():
    # Define the GStreamer pipeline for RTMP streaming
    rtmp_pipeline = (
        "nvarguscamerasrc sensor-id=0 ! "
        "video/x-raw(memory:NVMM),width=1920,height=1080,framerate=60/1 ! "
        "nvvidconv ! "
        "video/x-raw,format=BGR ! "
        "omxh264enc bitrate=3000000 ! "
        "flvmux ! "
        "rtmpsink location='rtmp://172.104.157.70:1936/ptz/testcam311'"
    )

    # Start the RTMP streaming process
    subprocess.Popen(rtmp_pipeline.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Define the GStreamer pipeline for OpenCV display
    display_pipeline = (
        "nvarguscamerasrc sensor-id=0 ! "
        "video/x-raw(memory:NVMM),width=1920,height=1080,framerate=60/1 ! "
        "nvvidconv ! "
        "video/x-raw,format=BGR ! "
        "appsink"
    )

    # Create a VideoCapture object for local display
    cap = cv2.VideoCapture(display_pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Display the resulting frame
        cv2.imshow('Camera Stream', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_camera_stream()
