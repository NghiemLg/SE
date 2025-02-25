# YOLOv11 Live Video Object Detection

This project demonstrates real-time object detection using the YOLOv11 model on a live video stream.

## Features

- Detects objects in real-time using YOLOv11.
- Draws bounding boxes and labels on detected objects.
- Supports various YOLOv11 model variants (e.g., `yolo11n.pt`, `yolo11s.pt`, `yolo11m.pt`).

## Requirements

- Python 3.8+
- [Ultralytics YOLO](https://docs.ultralytics.com) library
- OpenCV for video processing

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yolov11-video-detection.git
   cd yolov11-video-detection
   ```

2. **Install the required packages:**
   ```bash
   pip install ultralytics opencv-python
   ```

## Usage

1. **Set the video stream URL:**
   - Edit the `video_url` variable in `yolov11_video_detection.py`:
   ```python
   video_url = 'http://your_video_stream_url'  # Replace with your actual video stream URL
   ```

2. **Run the detection script:**
   ```bash
   python yolov11_video_detection.py
   ```

3. **Exit the video stream:**
   - Press `q` while the video window is active to stop the stream.

## Model Variants

You can choose different YOLOv11 models depending on your requirements:

- `yolo11n.pt`: Nano version (fastest, least accurate)
- `yolo11s.pt`: Small version (balanced speed and accuracy)
- `yolo11m.pt`: Medium version (higher accuracy, slower performance)

To switch models, change the following line in `yolov11_video_detection.py`:
```python
model = YOLO('yolo11s.pt')
```

## Troubleshooting

- **Cannot open video stream:**
  - Ensure the video URL is valid and accessible.
  - Check your internet connection.
  
- **Slow performance:**
  - Use a lighter model variant (e.g., `yolo11n.pt`).
  - Reduce the video resolution.

## License

This project is licensed under the MIT License.

