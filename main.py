import cv2
import socket
import pickle
import struct

def camera_demo():
    # Open the default camera
    print("Connecting...")
    cap = cv2.VideoCapture('rtmp://172.104.157.70:1936/ptz/testcam311')

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    else:
        print("Connected.")

    # Set up UDP socket
    udp_ip = "178.133.56.254"  # Change to the receiver's IP address
    udp_port = 12345           # Change to your desired port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Serialize the frame
        data = pickle.dumps(frame)
        # Send the frame size first
        sock.sendto(struct.pack("L", len(data)), (udp_ip, udp_port))

        for i in range(0, len(data), 4096):  # Adjust chunk size as needed
            try:
                sock.sendto(data[i:i + 4096], (udp_ip, udp_port))
            except Exception as e:
                print(f"Error sending frame data: {e}")
        print("Frame sent")

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    sock.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_demo()
