### 📄 **README: Video Stream Detection and Monitoring System**

#### **Overview**

This project includes three interconnected Python scripts for real-time video analysis using YOLO object detection and OpenCV. The system covers three key functionalities:  
1. **Real-time Object Detection from YouTube Stream**  
2. **Speed Estimation of Moving Objects**  
3. **Security Alarm with Email Notification**

These tools simulate a comprehensive **System Engineer** solution where video processing, real-time monitoring, and automated alerts are integrated for advanced surveillance and analytics.

---

### 🔍 **1. Real-Time Object Detection from YouTube Stream**

**File:** `youtube_yolo_stream.py`

**Purpose:**  
- This script streams a live YouTube video and uses YOLOv8 to detect objects in real-time.  
- It is useful for real-time monitoring systems that require analyzing live feeds.

**Key Features:**  
- Streams YouTube videos using `yt_dlp`.  
- Detects and highlights objects using pre-trained YOLOv8 models.  
- Displays detection results frame by frame.

**Usage:**  
Update the `video_url` with a valid YouTube video link. Run the script to start object detection in real-time.  

**Relation to System Engineering:**  
Simulates real-world use cases of live surveillance systems for traffic monitoring, wildlife observation, or industrial process monitoring.

---

### 🚗 **2. Speed Estimation of Moving Objects**

**File:** `speed_estimation.py`

**Purpose:**  
- Estimates the speed of detected objects (vehicles, persons) in a video.  
- This feature can be applied to traffic monitoring systems.

**Key Features:**  
- Processes video frames and estimates speed using object detection algorithms.  
- Allows custom region definition for speed estimation based on camera positioning.  
- Saves the output as a processed video.

**Usage:**  
- Replace `video_path` and `model_path` with actual file paths.  
- Adjust `speed_region` to fit your custom region of interest.  

**Relation to System Engineering:**  
Useful for developing Intelligent Transportation Systems (ITS) where real-time speed estimation is crucial for monitoring and managing traffic flow.

---

### 🔔 **3. Security Alarm with Email Notification**

**File:** `security_alarm.py`

**Purpose:**  
- Detects unusual activities through a live camera feed and sends an email notification if any suspicious activity is detected.

**Key Features:**  
- Uses YOLOv11 for detecting intrusions or unauthorized access.  
- Sends automated email alerts upon detecting a predefined number of events.  
- Records the surveillance video for later review.

**Usage:**  
- Update the sender and receiver email addresses.  
- Use a Google App Password for authentication (as Google requires this for third-party apps).  
- Connect a camera or webcam and run the script for real-time monitoring.

**Relation to System Engineering:**  
Demonstrates how system engineers can integrate real-time detection and alert mechanisms to ensure safety in industrial, residential, or commercial premises.

---

### 🔗 **Project Dependencies**

Ensure you have the following Python libraries installed:
- `opencv-python`
- `yt_dlp`
- `ultralytics`
- `numpy`
- `smtplib` (for email sending)

You can install the dependencies using:  
```bash
pip install opencv-python yt_dlp ultralytics numpy
```

---

### ⚙️ **How They Are Connected**

These scripts work together to build a robust **video analysis system**:
- **Live detection** feeds can be used as input for **speed estimation** or **security alarm** functionalities.  
- Speed estimation can trigger alerts or logs if an object surpasses a speed threshold.  
- The security alarm can be integrated with the object detection stream for better surveillance.

---

### 👨‍💻 **Why This Matters for a System Engineer**

As a **System Engineer**, integrating different systems—such as live video streams, real-time detection, speed estimation, and automated notifications—demonstrates the ability to design scalable, efficient, and reliable monitoring solutions. This project reflects essential skills like:  
- **System Integration**  
- **Automation**  
- **Real-Time Data Processing**  
- **Alert Systems Development**

---

### 🚀 **Future Enhancements**
- Deploy on embedded systems like Raspberry Pi for edge computing.  
- Integrate cloud-based storage for video recordings.  
- Add AI-based anomaly detection for smarter alerts.  

---
**Author:** ルオン・ザ・ギエム  
**License:** MIT
