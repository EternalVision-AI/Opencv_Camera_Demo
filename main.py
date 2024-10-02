import subprocess

def start_camera_stream():
    # Define the GStreamer command
    command = [
        "gst-launch-1.0",
        "nvarguscamerasrc", "sensor-id=0",
        "!", "video/x-raw(memory:NVMM),width=1920,height=1080,framerate=60/1",
        "!", "nvvidconv",
        "!", "video/x-raw(memory:NVMM),format=(string)I420",
        "!", "omxh264enc", "bitrate=3000000",
        "!", "flvmux",
        "!", "rtmpsink", "location='rtmp://172.104.157.70:1936/ptz/testcam311'"
    ]

    # Start the GStreamer process
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        # Optionally, read stdout and stderr if needed
        stdout, stderr = process.communicate()
        print(stdout.decode())
        print(stderr.decode())
    except KeyboardInterrupt:
        # Handle process termination
        process.terminate()
        print("Stream stopped.")

if __name__ == "__main__":
    start_camera_stream()
