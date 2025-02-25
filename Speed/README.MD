# Speed Estimation using YOLOv11

This project demonstrates vehicle speed estimation using the YOLOv11 model on video files.

## Features

- Detects vehicles using a custom-trained YOLOv11 model.
- Estimates and displays the speed of detected vehicles in real-time.
- Supports customizable detection regions and output formats.

## Requirements

- Python 3.8+
- [Ultralytics YOLO](https://docs.ultralytics.com) library
- OpenCV for video processing

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yolov11-speed-estimation.git
   cd yolov11-speed-estimation
   ```

2. **Install required packages:**
   ```bash
   pip install ultralytics opencv-python
   ```

## Usage

1. **Edit the script parameters:**
   - Set the paths and region in `yolov11_speed_estimation.py`:
   ```python
   video_path = "/path/to/your/video.mp4"  # Path to your video file
   model_path = "/path/to/your/model.engine"  # Path to your YOLOv11 model
   output_path = "output_speed_estimation.avi"  # Output video file
   speed_region = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  # Region for speed estimation
   ```

2. **Run the speed estimation script:**
   ```bash
   python yolov11_speed_estimation.py
   ```

3. **Exit:**
   - The processed video will be saved automatically to the defined output path.

## Customization

- **Change detection classes:**
  - You can configure the model to detect specific vehicle classes by modifying the `classes` parameter.

- **Adjust the speed region:**
  - Modify the `speed_region` variable to define a new area in the video frame for speed estimation.

## Troubleshooting

- **Video file not opening:**
  - Ensure the path to the video file is correct.
  - Check that the video format is supported.

- **Slow performance:**
  - Use a smaller model variant or reduce the video resolution.

## License

This project is licensed under the MIT License.

