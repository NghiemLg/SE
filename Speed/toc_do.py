# -*- coding: utf-8 -*-

import cv2
from ultralytics import solutions

def main(video_path, model_path, output_path, speed_region):
    # Open video capture
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), f"Error reading video file: {video_path}"
    
    # Get video properties
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    
    # Initialize video writer
    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
    
    # Initialize speed estimator
    speed = solutions.SpeedEstimator(
        show=True,  # Display the output
        model=model_path,  # Path to the YOLOv11 model file
        region=speed_region,  # Define region points for speed estimation
    )
    
    # Process video frames
    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("Video frame is empty or video processing has been successfully completed.")
            break
        
        # Estimate speed
        out = speed.estimate_speed(im0)
        video_writer.write(im0)
    
    # Release resources
    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "/path/to/your/video.mp4"  # Replace with the path to your video file
    model_path = "/path/to/your/model.engine"  # Replace with the path to your YOLOv11 model file
    output_path = "output_speed_estimation.avi"  # Output video file
    speed_region = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  # Define your custom region points
    
    main(video_path, model_path, output_path, speed_region)
