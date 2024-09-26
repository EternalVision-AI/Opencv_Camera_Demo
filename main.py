import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(311)

if not cap.isOpened():
    print("Error opening camera")

count = 0
# infinite loop until user decides to stop the program execution
while True:
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    count += 1
    print(count)
    # Display the resulting frame
    # cv2.imshow('Video Capture', frame)

    # if 'q' is pressed on the keyboard, 
    # stop capturing frames and close all windows
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the VideoCapture object
# cap.release()
# cv2.destroyAllWindows()
