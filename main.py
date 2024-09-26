import cv2

# Access the Arducam CSI camera
# cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(3840), height=(2160), format=(NV12), framerate=(30/1) ! nvvidconv ! video/x-raw, format=(BGRx) ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    print("Running...")
    # cv2.imshow('Arducam Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
