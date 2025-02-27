# README

## Overview
This code sets up a simple security camera system using the YOLO model for object detection and sends email notifications when motion or specific objects are detected. It processes video from a camera feed, analyzes it in real-time, and saves the output to a video file.

## Requirements

- Python 3.x
- OpenCV
- Ultraytics package
- Email credentials for authentication (Gmail recommended)

## Libraries Used

- **cv2**: Used to capture video and process frames.
- **ultralytics**: Provides access to pre-trained object detection models (e.g., YOLO).

## Installation

To run this script, you need to install the required libraries. You can install them via `pip`:

```bash
pip install opencv-python ultralytics
```

## Usage

1. **Setup Video Capture:**
   - The script uses the default webcam (`cv2.VideoCapture(0)`). If you want to use a different camera or a video file, change the argument passed to `cv2.VideoCapture`.

2. **Email Setup:**
   - Replace `from_email` with your email address.
   - Set `password` to a 16-digit app password (generated via [Google App Passwords](https://myaccount.google.com/apppasswords)).
   - Set `to_email` to the email address where you want to receive notifications.

3. **YOLO Model:**
   - The model used is `yolo11n.pt`. You can replace this with your own YOLO model if necessary.

4. **Running the Script:**
   - Once the script is executed, it captures video from the camera, processes each frame to detect objects, and writes the processed frames into `security_alarm_output.avi`.
   - When the `SecurityAlarm` system detects an object, it will send an email notification.

5. **Output:**
   - The processed video is saved as `security_alarm_output.avi`.
   - If an object is detected, the system will send an email notification.

## Notes

- Ensure your email provider allows app passwords (for Gmail, you may need to enable two-factor authentication and generate an app password).
- You may need to modify the security alarm configuration based on the specific model and detection parameters you wish to use.

## Example:

```bash
python security_alarm.py
```

This will start the security camera system and process the video feed in real time, sending an email if any objects are detected. The output video will be saved as `security_alarm_output.avi`.

## License

This project is licensed under the MIT License.
