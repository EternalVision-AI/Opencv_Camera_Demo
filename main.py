import cv2
import time

def camera_demo():
    # Open the default camera (usually the first camera, index 0)
    print("Connecting...")
    cap = cv2.VideoCapture('rtmp://172.104.157.70:1936/ptz/testcam311')

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    else:
        print("Connected.")

    fps = 0
    frame_count = 0
    start_time = time.time()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Increment frame count
        frame_count += 1

        # Calculate FPS every second
        if time.time() - start_time >= 1:
            fps = frame_count
            frame_count = 0
            start_time = time.time()

        # Display the FPS on the frame
        # cv2.putText(frame, f'FPS: {fps}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the resulting frame
        # cv2.imshow('Camera Demo', frame)
        print("FPS: ", str(fps))
        print("Frame: ", str(frame.shape))

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_demo()
